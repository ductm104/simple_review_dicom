import PySimpleGUI as sg
import time
import imageio
import json
import imageio
import cv2
import numpy as np
from PIL import Image, ImageSequence


class VideoLayout:
    WIDTH = 640
    HEIGHT = 480

    def __init__(self):
        self.file_data = None

        self.viewer = sg.Image(size=(self.WIDTH, self.HEIGHT),
                               #enable_events=True,
                               background_color='black',)
        self.layout = [
                [self.viewer],
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

    def on_change(self, file_data):
        if self.file_data is not None and self.file_data[0] == file_data[0]:
            return
        self.file_data = file_data
        self.mp4 = imageio.get_reader(file_data[3], 'ffmpeg')
        #self.mp4 = [cv2.resize(x, (640, 480)) for x in self.mp4]
        self.frames = list(map(lambda x: cv2.imencode('.png', x)[1].tobytes(), self.mp4))

        self.__reset()
    
    def __reset(self):
        self.frame_index = 0
        self.num_frame = len(self.frames)

    def update(self):
        if self.file_data is None:
            return
        self.frame_index = (self.frame_index + 1) % self.num_frame
        data = self.frames[self.frame_index]
        self.viewer.update(data=data)
