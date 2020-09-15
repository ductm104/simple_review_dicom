import PySimpleGUI as sg
import time
import imageio
import json
import imageio
import cv2
import numpy as np

from PIL import Image, ImageSequence
from config import PLAY_PAUSE_PREFIX
from concurrent.futures import ThreadPoolExecutor


class VideoLayout:
    WIDTH = 640
    HEIGHT = 480

    def __init__(self):
        self.file_data = None
        self.is_playing = False

        self.viewer = sg.Image(size=(self.WIDTH, self.HEIGHT),
                               background_color='black',)

        self.frame_text = sg.Text(size=(30, 1),
                                  text_color='yellow',
                                  justification='center',
                                  font=('Helvetica', 13))

        self.play_button = sg.B('PAUSE', enable_events=True,
                                border_width=3,
                                key=PLAY_PAUSE_PREFIX+'-PLAY',
                                font=('Helvetica', 10, "bold"),
                                button_color=('red', None))

        self.layout = [
                [self.viewer],
                [self.frame_text],
                [
                    sg.B('PREV', enable_events=True,
                         font=('Helvetica', 10),
                         key=PLAY_PAUSE_PREFIX+'-PREV',
                         border_width=3),
                    self.play_button,
                    sg.B('NEXT', enable_events=True,
                         font=('Helvetica', 10),
                         key=PLAY_PAUSE_PREFIX+'-NEXT',
                         border_width=3), 
                ],
        ]

        self.fviewer = sg.Frame('Video Player',
                            layout=self.layout,
                            title_color='blue',
                            font=('Helvetica', 15),
                            border_width=5,
                            vertical_alignment='top',
                            element_justification='center',)

    def get_layout(self):
        return self.fviewer

    def __encode_video(self, mp4):
        def encode(img):
            return cv2.imencode('.png', img)[1].tobytes()
        with ThreadPoolExecutor(8) as pool:
            frames = list(pool.map(encode, mp4))
        return frames
    
    def on_change(self, file_data):
        if self.file_data is not None and self.file_data[0] == file_data[0]:
            return

        self.file_data = file_data
        self.mp4 = imageio.get_reader(file_data[3], 'ffmpeg')
        self.frames = self.__encode_video(self.mp4)

        self.__reset()
    
    def __reset(self):
        self.is_playing = True
        self.frame_index = 0
        self.num_frame = len(self.frames)

    def __update(self):
        if self.file_data is None:
            return
        
        if self.is_playing is True:
            self.frame_index = (self.frame_index + 1) % self.num_frame

        self.frame_text.update(value=f'Frame {self.frame_index+1}')
        data = self.frames[self.frame_index]
        self.viewer.update(data=data)

    def __prev_next(self, value):
        if self.is_playing is False and self.file_data is not None:
            self.frame_index = (self.frame_index+value) % self.num_frame

    def update(self, event, values):
        if PLAY_PAUSE_PREFIX in event:
            action = event.split('-')[-1]
            if action == 'PLAY':
                self.__play_pause()
            if action == 'PREV':
                self.__prev_next(-1)
            if action == 'NEXT':
                self.__prev_next(1)
        self.__update()

    def __play_pause(self):
        if self.file_data is None:
            return

        if self.is_playing is True:
            self.is_playing = False
            self.play_button.update(text='PLAY', button_color=('green', None))
        else:
            self.is_playing = True
            self.play_button.update(text='PAUSE', button_color=('red', None))
