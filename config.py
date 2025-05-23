# Path configurations

import cv2

MODEL_PATH = "Weights//3000_best (60single).pt"
OUTPUT_PATH = "Bottle_image_yolo_v_11_DYP//output"

# VIDEO_PATH = "D://Projects//Python//Bottle_measurement//input//Video copy.mp4"
VIDEO_PATH= "input//v1.mp4"
# VIDEO_PATH="input//v2.mp4"
# VIDEO_PATH = "input//v3.mp4"
# VIDEO_PATH = "input//v4.mp4"

     



# Detection settings
CLASS_NAMES = {0: 'defect', 1: 'bottle', 2: 'bottle_neck'}
MM_PER_PIXEL = 0.092  # Calibration factor
CONF_THRESHOLD = 0.2

# Display settings
FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.8
FONT_THICKNESS = 2
LINE_HEIGHT = 25
COLORS = {
    'defect': (0, 0, 255),
    'bottle': (255, 0, 0),
    'bottle_neck': (0, 255, 0)
}

# Video settings
DISPLAY_SIZE = (600, 800)
ROTATE_VIDEO = True
# ROTATE_VIDEO = False



################
### new addition
# Add rotation flag and maintain original video settings
# ROTATE_VIDEO = True  # Set False if you want original orientation
# ORIGINAL_WIDTH = 1280
# ORIGINAL_HEIGHT = 720


