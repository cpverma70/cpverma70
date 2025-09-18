import cv2
import threading
import time
from config import Config

class CameraManager:
    def __init__(self, camera_index=None):
        """
        Initialize camera manager.
        
        Args:
            camera_index: Camera index (default from config)
        """
        self.camera_index = camera_index if camera_index is not None else Config.CAMERA_INDEX
        self.frame_width = Config.FRAME_WIDTH
        self.frame_height = Config.FRAME_HEIGHT
        
        self.cap = None
        self.current_frame = None
        self.is_running = False
        self.frame_lock = threading.Lock()
        self.capture_thread = None
        
    def start_camera(self):
        """Start the camera and begin capturing frames."""
        try:
            print(f"Starting camera {self.camera_index}...")
            
            # Initialize camera
            self.cap = cv2.VideoCapture(self.camera_index)
            
            if not self.cap.isOpened():
                print(f"❌ Error: Could not open camera {self.camera_index}")
                return False
            
            # Set camera properties
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)
            self.cap.set(cv2.CAP_PROP_FPS, 30)
            
            # Test camera
            ret, test_frame = self.cap.read()
            if not ret:
                print("❌ Error: Could not read from camera")
                self.cap.release()
                return False
            
            print(f"✅ Camera started successfully")
            print(f"Frame size: {test_frame.shape[1]}x{test_frame.shape[0]}")
            
            # Start capture thread
            self.is_running = True
            self.capture_thread = threading.Thread(target=self._capture_loop)
            self.capture_thread.daemon = True
            self.capture_thread.start()
            
            return True
            
        except Exception as e:
            print(f"❌ Error starting camera: {e}")
            return False
    
    def _capture_loop(self):
        """Main capture loop running in separate thread."""
        while self.is_running and self.cap is not None:
            try:
                ret, frame = self.cap.read()
                if ret:
                    with self.frame_lock:
                        self.current_frame = frame.copy()
                else:
                    print("⚠️ Warning: Failed to read frame from camera")
                    time.sleep(0.1)  # Brief pause before retrying
                    
            except Exception as e:
                print(f"Error in capture loop: {e}")
                time.sleep(0.1)
    
    def get_frame(self):
        """
        Get the latest frame from camera.
        
        Returns:
            numpy.ndarray or None: Latest frame or None if not available
        """
        with self.frame_lock:
            if self.current_frame is not None:
                return self.current_frame.copy()
            return None
    
    def stop_camera(self):
        """Stop the camera and cleanup resources."""
        print("Stopping camera...")
        self.is_running = False
        
        # Wait for capture thread to finish
        if self.capture_thread and self.capture_thread.is_alive():
            self.capture_thread.join(timeout=2)
        
        # Release camera
        if self.cap:
            self.cap.release()
            self.cap = None
        
        print("✅ Camera stopped")
    
    def is_camera_available(self):
        """Check if camera is available and working."""
        return self.is_running and self.cap is not None and self.cap.isOpened()
    
    def get_camera_info(self):
        """Get camera information."""
        if not self.cap:
            return None
            
        info = {
            'index': self.camera_index,
            'width': int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            'height': int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
            'fps': int(self.cap.get(cv2.CAP_PROP_FPS)),
            'is_opened': self.cap.isOpened()
        }
        return info
    
    @staticmethod
    def list_available_cameras(max_cameras=10):
        """
        List all available cameras.
        
        Args:
            max_cameras: Maximum number of cameras to check
            
        Returns:
            list: List of available camera indices
        """
        available_cameras = []
        
        print("Scanning for available cameras...")
        for i in range(max_cameras):
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                ret, _ = cap.read()
                if ret:
                    available_cameras.append(i)
                    print(f"✅ Camera {i}: Available")
                else:
                    print(f"⚠️ Camera {i}: Opened but cannot read")
            else:
                print(f"❌ Camera {i}: Not available")
            cap.release()
        
        return available_cameras
    
    def test_camera(self, duration=5):
        """
        Test camera by displaying frames for a specified duration.
        
        Args:
            duration: Test duration in seconds
        """
        if not self.is_camera_available():
            print("❌ Camera not available for testing")
            return False
        
        print(f"Testing camera for {duration} seconds...")
        print("Press 'q' to quit early")
        
        start_time = time.time()
        frame_count = 0
        
        while time.time() - start_time < duration:
            frame = self.get_frame()
            if frame is not None:
                frame_count += 1
                
                # Add test overlay
                cv2.putText(frame, f"Camera Test - Frame: {frame_count}", 
                           (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                cv2.putText(frame, f"Time: {time.time() - start_time:.1f}s", 
                           (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                cv2.putText(frame, "Press 'q' to quit", 
                           (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
                
                cv2.imshow('Camera Test', frame)
                
                # Check for quit key
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                print("⚠️ No frame available")
                time.sleep(0.1)
        
        cv2.destroyAllWindows()
        
        fps = frame_count / (time.time() - start_time)
        print(f"✅ Camera test completed")
        print(f"Frames captured: {frame_count}")
        print(f"Average FPS: {fps:.2f}")
        
        return True