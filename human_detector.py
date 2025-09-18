import cv2
import numpy as np
from ultralytics import YOLO
import time
from config import Config

class HumanDetector:
    def __init__(self):
        """Initialize the human detector with YOLO model."""
        print("Loading YOLO model...")
        self.model = YOLO('yolov8n.pt')  # Using YOLOv8 nano for speed
        self.confidence_threshold = Config.CONFIDENCE_THRESHOLD
        self.last_detection_time = 0
        self.cooldown_period = Config.DETECTION_COOLDOWN
        
    def detect_humans(self, frame):
        """
        Detect humans in the given frame.
        
        Args:
            frame: OpenCV image frame
            
        Returns:
            tuple: (human_detected: bool, annotated_frame: np.array, detections: list)
        """
        # Run YOLO inference
        results = self.model(frame, verbose=False)
        
        human_detected = False
        detections = []
        
        # Process results
        for result in results:
            boxes = result.boxes
            if boxes is not None:
                for box in boxes:
                    # Get class ID and confidence
                    class_id = int(box.cls[0])
                    confidence = float(box.conf[0])
                    
                    # Check if it's a person (class_id = 0 in COCO dataset)
                    if class_id == 0 and confidence >= self.confidence_threshold:
                        human_detected = True
                        
                        # Get bounding box coordinates
                        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                        detections.append({
                            'bbox': (int(x1), int(y1), int(x2), int(y2)),
                            'confidence': confidence
                        })
        
        # Annotate frame with detections
        annotated_frame = self._annotate_frame(frame, detections)
        
        return human_detected, annotated_frame, detections
    
    def _annotate_frame(self, frame, detections):
        """Annotate frame with bounding boxes and labels."""
        annotated_frame = frame.copy()
        
        for detection in detections:
            x1, y1, x2, y2 = detection['bbox']
            confidence = detection['confidence']
            
            # Draw bounding box
            cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # Draw label
            label = f"Human: {confidence:.2f}"
            label_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)[0]
            cv2.rectangle(annotated_frame, (x1, y1 - label_size[1] - 10), 
                         (x1 + label_size[0], y1), (0, 255, 0), -1)
            cv2.putText(annotated_frame, label, (x1, y1 - 5), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        
        return annotated_frame
    
    def should_trigger_alert(self, human_detected):
        """
        Check if an alert should be triggered based on detection and cooldown.
        
        Args:
            human_detected: Boolean indicating if human was detected
            
        Returns:
            bool: True if alert should be triggered
        """
        current_time = time.time()
        
        if human_detected and (current_time - self.last_detection_time) > self.cooldown_period:
            self.last_detection_time = current_time
            return True
        
        return False