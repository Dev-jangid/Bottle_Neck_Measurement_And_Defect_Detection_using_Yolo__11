import cv2
import config

def draw_measurements(frame, result):
    neck_data = []
    boxes = result.boxes.xyxy.cpu().numpy()
    classes = result.boxes.cls.cpu().numpy()
    confidences = result.boxes.conf.cpu().numpy()

    for box, cls, conf in zip(boxes, classes, confidences):
        x1, y1, x2, y2 = map(int, box)
        class_name = config.CLASS_NAMES.get(int(cls), 'defect')
        color = config.COLORS.get(class_name, (0, 0, 255))

        # Draw bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

        # Prepare label
        label = [f"{class_name} {conf:.2f}"]
        if class_name == 'bottle_neck':
            width_mm = (x2 - x1) * config.MM_PER_PIXEL
            height_mm = (y2 - y1) * config.MM_PER_PIXEL
            centroid = ((x1 + x2) // 2, (y1 + y2) // 2)
            neck_data.append((width_mm, height_mm, centroid))
            # label.append(f"W: {width_mm:.1f}mm H: {height_mm:.1f}mm")
            label.append(f"Length: {height_mm:.1f}mm Width: {width_mm:.1f}mm ")


        # Draw label
        draw_label(frame, x1, y1, label, color)

        # Draw centroid
        if class_name == 'bottle_neck':
            cv2.drawMarker(frame, centroid, color, 
                          markerType=cv2.MARKER_CROSS, 
                          markerSize=20, thickness=2)
    
    return neck_data

def draw_label(frame, x1, y1, lines, color):
    total_height = config.LINE_HEIGHT * len(lines)
    max_width = max(cv2.getTextSize(line, config.FONT, 
                     config.FONT_SCALE, config.FONT_THICKNESS)[0][0] 
                  for line in lines)
    
    # Label background
    y_start = max(y1 - total_height, 0)
    cv2.rectangle(frame, (x1, y_start), 
                 (x1 + max_width + 10, y_start + total_height), 
                 color, -1)
    
    # Label text
    for i, line in enumerate(lines):
        y = y_start + (i + 1) * config.LINE_HEIGHT - 7
        cv2.putText(frame, line, (x1 + 5, y),
                   config.FONT, config.FONT_SCALE,
                   (255, 255, 255), config.FONT_THICKNESS)



