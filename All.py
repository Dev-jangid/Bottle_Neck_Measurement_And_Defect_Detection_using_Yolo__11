
import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("D://Projects//Python//Bottle_measurement//Weights//3000_best (60single).pt")
class_names = {0: 'defect', 1: 'bottle', 2: 'bottle_neck'}

# Initialize video

cap = cv2.VideoCapture(1)
# cap = cv2.VideoCapture("D://Projects//Python//Bottle_measurement//input//Video 2.mp4")
# cap = cv2.VideoCapture("D://Projects//Python//Bottle_measurement//input//video.mp4")
# cap = cv2.VideoCapture("D://Projects//Python//Bottle_measurement//input//Video copy.mp4")
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Calibration factor (adjust based on your setup)
MM_PER_PIXEL = 0.12

# Font settings for bold, large labels
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.8
font_thickness = 2
line_height = 25

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO prediction
    results = model.predict(frame, conf=0.2, verbose=False)
    neck_measurements = []

    for result in results:
        boxes = result.boxes.xyxy.cpu().numpy()
        classes = result.boxes.cls.cpu().numpy()
        confidences = result.boxes.conf.cpu().numpy()

        for box, cls, conf in zip(boxes, classes, confidences):
            x1, y1, x2, y2 = map(int, box)
            class_id = int(cls)
            class_name = class_names.get(class_id, 'defects')
            confidence = float(conf)

            # Default color: red (defect)
            color = (0, 0, 255)
            label_lines = [f"{class_name} {confidence:.2f}"]

            if class_name == "bottle":
                color = (255, 0, 0)  # Blue

            elif class_name == "bottle_neck":
                color = (0, 255, 0)  # Green
                neck_width = (x2 - x1) * MM_PER_PIXEL
                neck_height = (y2 - y1) * MM_PER_PIXEL
                centroid = ((x1 + x2) // 2, (y1 + y2) // 2)
                neck_measurements.append((neck_width, neck_height, centroid))
                label_lines.append(f"Height: {neck_width:.1f}mm Length: {neck_height:.1f}mm")

            # Draw bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

            # Prepare label background
            total_height = line_height * len(label_lines)
            max_line_width = max(
                cv2.getTextSize(line, font, font_scale, font_thickness)[0][0]
                for line in label_lines
            )
            label_y = max(y1 - total_height, 0)
            cv2.rectangle(
                frame, 
                (x1, label_y), 
                (x1 + max_line_width + 10, label_y + total_height), 
                color, 
                -1
            )

            # Draw label text
            for i, line in enumerate(label_lines):
                y = label_y + (i + 1) * line_height - 7
                cv2.putText(frame, line, (x1 + 5, y), font, font_scale, (255, 255, 255), font_thickness)

            # Draw centroid marker for neck
            if class_name == "bottle_neck":
                cv2.drawMarker(frame, centroid, color, markerType=cv2.MARKER_CROSS, markerSize=20, thickness=2)


    # Display frame
    resized_frame = cv2.resize(frame, (600, 800))
    cv2.imshow('Bottle Inspection', resized_frame)
    # out.write(resized_frame)

    
    
    # Rotate and resize frame for display
    # rotated = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    # resized = cv2.resize(rotated, (600, 800))
    # cv2.imshow('Bottle Inspection', resized)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




