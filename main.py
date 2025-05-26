#### Code1 

import cv2
from detector import Detector
from utils import draw_measurements
import config

def main():
    # Initialize detector
    detector = Detector()
    cap = cv2.VideoCapture(config.VIDEO_PATH)
    # To use webcam instead, uncomment below:
    # cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print(f"Error: Unable to open video source {config.VIDEO_PATH}")
        return  

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Detect and annotate
        result = detector.detect(frame)
        neck_data = draw_measurements(frame, result)

        # Rotate frame if configured
        if config.ROTATE_VIDEO == True:
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            
      

        # Optionally overlay neck measurements in corner
        x_text, y_text = 10, 30
        line_height = 25
        for i, (w_mm, h_mm, _) in enumerate(neck_data):
            text = f"Bottle_Neck {i+1}: Length={h_mm:.1f}mm Width={w_mm:.1f}mm"
            y = y_text + i * line_height
            # cv2.putText(frame, text, (x_text, y), config.FONT, config.FONT_SCALE, (225, 255, 255), config.FONT_THICKNESS)
            cv2.putText(frame, text, (x_text, y), config.FONT, config.FONT_SCALE, (0,255,0), config.FONT_THICKNESS)


        # Resize for display
        display_frame = cv2.resize(frame, config.DISPLAY_SIZE)
        cv2.imshow('Bottle Inspection', display_frame)
        

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    # out.release()  # Uncomment if video writer is used
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()












    

#### Code 2  

# import cv2
# from detector import Detector
# from utils import draw_measurements
# import config

# def main():
#     # Initialize components
#     detector = Detector()
#     cap = cv2.VideoCapture(config.VIDEO_PATH)
#     # cap = cv2.VideoCapture(0)
    
#     # Removed VideoWriter setup and saving

#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Process frame
#         result = detector.detect(frame)
#         neck_data = draw_measurements(frame, result)
        
#         # Rotate frame if needed
#         if config.ROTATE_VIDEO:
#             frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

#         # Display
#         display_frame = cv2.resize(frame, config.DISPLAY_SIZE)
#         cv2.imshow('Bottle Inspection', display_frame)
        
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Cleanup
#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()






##### Code  3

# import cv2
# from detector import Detector
# from utils import draw_measurements
# import config

# def main():
#     # Initialize components
#     detector = Detector()
#     cap = cv2.VideoCapture(config.VIDEO_PATH)
#     # cap = cv2.VideoCapture(0)
    
#     # Video writer setup
#     frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#     out = cv2.VideoWriter(config.OUTPUT_PATH, fourcc,
#                          cap.get(cv2.CAP_PROP_FPS), 
#                          (frame_height, frame_width))  # Rotated dimensions

#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Process frame
#         result = detector.detect(frame)
#         neck_data = draw_measurements(frame, result)
        

#         # Save rotated frame
#         if config.ROTATE_VIDEO:
#             frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
#         out.write(frame)

#         # Display
#         display_frame = cv2.resize(frame, config.DISPLAY_SIZE)
#         cv2.imshow('Bottle Inspection', display_frame)
#         out.write(display_frame)
        
        

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Cleanup
#     cap.release()
#     out.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()
