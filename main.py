#!/usr/bin/env python3
"""
Human Detection AI App
A comprehensive security system that detects humans using AI and sends alerts
via sound alarm, WhatsApp, and email notifications.
"""

import cv2
import time
import signal
import sys
import argparse
from datetime import datetime

from human_detector import HumanDetector
from camera_manager import CameraManager
from alarm_system import AlarmSystem
from notification_system import NotificationSystem
from config import Config

class HumanDetectionApp:
    def __init__(self, camera_index=None, headless=False):
        """
        Initialize the Human Detection App.
        
        Args:
            camera_index: Camera index to use (default from config)
            headless: Run without GUI display
        """
        self.headless = headless
        self.is_running = False
        
        print("🤖 Initializing Human Detection AI App...")
        
        # Initialize components
        self.camera_manager = CameraManager(camera_index)
        self.human_detector = HumanDetector()
        self.alarm_system = AlarmSystem()
        self.notification_system = NotificationSystem()
        
        # Statistics
        self.total_detections = 0
        self.session_start_time = datetime.now()
        self.last_detection_time = None
        
        # Setup signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
        
        print("✅ Human Detection App initialized successfully!")
    
    def _signal_handler(self, signum, frame):
        """Handle shutdown signals gracefully."""
        print(f"\n🛑 Received signal {signum}, shutting down gracefully...")
        self.stop()
        sys.exit(0)
    
    def start(self):
        """Start the human detection system."""
        print("\n🚀 Starting Human Detection System...")
        
        # Start camera
        if not self.camera_manager.start_camera():
            print("❌ Failed to start camera. Exiting.")
            return False
        
        # Display camera info
        camera_info = self.camera_manager.get_camera_info()
        if camera_info:
            print(f"📷 Camera Info: {camera_info['width']}x{camera_info['height']} @ {camera_info['fps']}fps")
        
        self.is_running = True
        print("✅ System is now monitoring for humans...")
        print("📢 Notifications configured for:")
        if Config.WHATSAPP_RECIPIENTS:
            print(f"   📱 WhatsApp: {len(Config.WHATSAPP_RECIPIENTS)} recipients")
        if Config.EMAIL_RECIPIENTS:
            print(f"   📧 Email: {len(Config.EMAIL_RECIPIENTS)} recipients")
        
        if not self.headless:
            print("👁️ Press 'q' to quit, 's' for statistics, 't' to test notifications")
        
        try:
            self._main_loop()
        except KeyboardInterrupt:
            print("\n🛑 Interrupted by user")
        except Exception as e:
            print(f"❌ Error in main loop: {e}")
        finally:
            self.stop()
        
        return True
    
    def _main_loop(self):
        """Main detection loop."""
        fps_counter = 0
        fps_start_time = time.time()
        
        while self.is_running:
            # Get frame from camera
            frame = self.camera_manager.get_frame()
            if frame is None:
                time.sleep(0.1)
                continue
            
            # Detect humans
            human_detected, annotated_frame, detections = self.human_detector.detect_humans(frame)
            
            # Process detections
            if human_detected:
                self._handle_detection(detections, annotated_frame)
            
            # Display frame if not headless
            if not self.headless:
                self._display_frame(annotated_frame, human_detected, len(detections))
                
                # Handle keyboard input
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    print("\n👋 Quitting...")
                    break
                elif key == ord('s'):
                    self._print_statistics()
                elif key == ord('t'):
                    self._test_notifications()
            else:
                # Small delay for headless mode
                time.sleep(0.03)  # ~30 FPS
            
            # FPS calculation
            fps_counter += 1
            if fps_counter % 30 == 0:  # Update every 30 frames
                current_time = time.time()
                fps = fps_counter / (current_time - fps_start_time)
                if not self.headless:
                    print(f"📊 FPS: {fps:.1f}")
                fps_counter = 0
                fps_start_time = current_time
    
    def _handle_detection(self, detections, frame):
        """Handle human detection event."""
        detection_count = len(detections)
        confidence_scores = [det['confidence'] for det in detections]
        
        # Check if we should trigger alerts (respects cooldown)
        if self.human_detector.should_trigger_alert(True):
            self.total_detections += 1
            self.last_detection_time = datetime.now()
            
            print(f"\n🚨 HUMAN DETECTED! Count: {detection_count}, Max Confidence: {max(confidence_scores):.2f}")
            
            # Trigger sound alarm
            self.alarm_system.play_alarm(duration=3)
            
            # Send notifications
            self.notification_system.send_detection_alert(
                detection_count=detection_count,
                confidence_scores=confidence_scores,
                frame=frame
            )
            
            print("📢 Alerts sent!")
    
    def _display_frame(self, frame, human_detected, detection_count):
        """Display frame with overlay information."""
        display_frame = frame.copy()
        
        # Add status overlay
        status_color = (0, 0, 255) if human_detected else (0, 255, 0)
        status_text = f"HUMAN DETECTED ({detection_count})" if human_detected else "MONITORING"
        
        cv2.putText(display_frame, status_text, (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, status_color, 2)
        
        # Add timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cv2.putText(display_frame, timestamp, (10, display_frame.shape[0] - 40), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        # Add session info
        session_time = (datetime.now() - self.session_start_time).total_seconds()
        session_info = f"Session: {session_time:.0f}s | Detections: {self.total_detections}"
        cv2.putText(display_frame, session_info, (10, display_frame.shape[0] - 20), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
        
        # Add controls
        cv2.putText(display_frame, "Press: 'q'=quit, 's'=stats, 't'=test", 
                   (10, display_frame.shape[0] - 5), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255), 1)
        
        cv2.imshow('Human Detection System', display_frame)
    
    def _print_statistics(self):
        """Print system statistics."""
        session_duration = (datetime.now() - self.session_start_time).total_seconds()
        
        print("\n📊 === SYSTEM STATISTICS ===")
        print(f"Session Duration: {session_duration:.0f} seconds")
        print(f"Total Detections: {self.total_detections}")
        if self.last_detection_time:
            print(f"Last Detection: {self.last_detection_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Detection Rate: {self.total_detections / (session_duration / 60):.2f} per minute")
        print(f"Camera: {self.camera_manager.get_camera_info()}")
        print("========================\n")
    
    def _test_notifications(self):
        """Test notification systems."""
        print("\n🧪 Testing notification systems...")
        self.notification_system.test_notifications()
        self.alarm_system.test_alarm()
        print("Test completed!\n")
    
    def stop(self):
        """Stop the detection system."""
        if not self.is_running:
            return
        
        print("\n🛑 Stopping Human Detection System...")
        self.is_running = False
        
        # Stop components
        self.camera_manager.stop_camera()
        self.alarm_system.stop_alarm()
        
        # Close OpenCV windows
        cv2.destroyAllWindows()
        
        # Print final statistics
        self._print_statistics()
        print("✅ System stopped successfully!")

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Human Detection AI Security System')
    parser.add_argument('--camera', type=int, default=None, 
                       help='Camera index to use (default: from config)')
    parser.add_argument('--headless', action='store_true', 
                       help='Run without GUI display')
    parser.add_argument('--test-camera', action='store_true', 
                       help='Test camera and exit')
    parser.add_argument('--list-cameras', action='store_true', 
                       help='List available cameras and exit')
    parser.add_argument('--test-notifications', action='store_true', 
                       help='Test notification systems and exit')
    parser.add_argument('--test-alarm', action='store_true', 
                       help='Test alarm system and exit')
    
    args = parser.parse_args()
    
    # Handle utility commands
    if args.list_cameras:
        print("🔍 Scanning for available cameras...")
        cameras = CameraManager.list_available_cameras()
        if cameras:
            print(f"✅ Found {len(cameras)} available camera(s): {cameras}")
        else:
            print("❌ No cameras found")
        return
    
    if args.test_notifications:
        print("🧪 Testing notification systems...")
        notifier = NotificationSystem()
        notifier.test_notifications()
        return
    
    if args.test_alarm:
        print("🧪 Testing alarm system...")
        alarm = AlarmSystem()
        alarm.test_alarm()
        time.sleep(5)  # Wait for test to complete
        return
    
    if args.test_camera:
        print("🧪 Testing camera...")
        camera = CameraManager(args.camera)
        if camera.start_camera():
            camera.test_camera(duration=10)
            camera.stop_camera()
        return
    
    # Main application
    print("🤖 Human Detection AI Security System")
    print("====================================")
    
    # Check configuration
    if not Config.EMAIL_RECIPIENTS and not Config.WHATSAPP_RECIPIENTS:
        print("⚠️ WARNING: No notification recipients configured!")
        print("Please edit .env file to add email and/or WhatsApp recipients.")
    
    # Start the application
    app = HumanDetectionApp(camera_index=args.camera, headless=args.headless)
    app.start()

if __name__ == "__main__":
    main()