DICOM_ROOT = '/media/tuan/DATA/AI-Cardio/dicom_data_20200821_map_bv/train'
REPRESENTATION_ROOT = '/media/tuan/DATA/AI-Cardio/dicom_data_20200821_map_bv/representation'

# JSON_PATH = '/media/tuan/DATA/Duc_Tools/ReviewLevelData/train_20200820_4011_cases_72730_files.json'
JSON_PATH = "/media/tuan/DATA/AI-Cardio/modules/ReviewLevelData/train_20200820_4011_cases_72730_files.json"

# OUT_JSON_PATH = '/media/tuan/DATA/Duc_Tools/ReviewLevelData/src/checklist.json'
OUT_JSON_PATH = "/media/tuan/DATA/AI-Cardio/modules/ReviewLevelData/src/checklist_dev.json"


WINDOW_CONFIG = {
    "title": "Dicom viewer by DucTM feat TuanNM",
    "location": (50, 50),
    "text_justification": "center",
    #"grab_anywhere": True,
    "resizable": True,
    "size": (1696, 960),
}
WINDOW_TIMEOUT = 20


GRID_PREFIX = 'GRID_LAYOUT'
PLAYER_PREFIX = 'PLAYER_LAYOUT'
ANNOTATION_PREFIX = 'ANNOTATION_PREFIX'
VIDEO_PLAYER_PREFIX = 'VIDEO_LAYER_PREFIX'
CHECKBOX_PREFIX = 'CHECKBOX_PREFIX'
CHOOSE_CASE_PREFIX = 'CHOOSE_CASE_PREFIX'
SAVE_ALL_PREFIX = 'SAVE_ALL_PREFIX'
COMMENT_PREFIX = 'COMMENT_PREFIX'
NOT_REVIEW_PREFIX = 'NOT_REVIEW_PREFIX'
DROP_DOWN_CHAMBER = 'DROP_DOWN_CHAMBER'
PLAY_PAUSE_PREFIX = 'PLAY_PAUSE_PREIX'


JSON_ORDER_MAPPING = {
    'no_defined': 1,
    'bad': 2,
    'vinif': 3,
    'kc': 4,
    'other': 5,
    'no_chamber': 6,
    '3d': 7,
    'none': 8,
}

# mapping = {99: "not_view", 0: "other", 1: "no_chamber", 2: "bad", 3:"vinif", 4:"kc"}
