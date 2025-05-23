from ultralytics import YOLO
import config

class Detector:
    def __init__(self):
        self.model = YOLO(config.MODEL_PATH)
        
    def detect(self, frame):
        results = self.model.predict(
            frame, 
            conf=config.CONF_THRESHOLD, 
            verbose=False
        )
        return results[0]  # Return first (and only) result