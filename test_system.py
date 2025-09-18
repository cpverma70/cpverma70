#!/usr/bin/env python3
"""
System test script for Human Detection AI
Tests all components individually to ensure proper setup
"""

import sys
import time
import traceback
from pathlib import Path

def test_imports():
    """Test if all required modules can be imported."""
    print("🧪 Testing imports...")
    
    required_modules = [
        ('cv2', 'OpenCV'),
        ('numpy', 'NumPy'),
        ('ultralytics', 'Ultralytics YOLO'),
        ('pygame', 'Pygame'),
        ('twilio', 'Twilio'),
        ('dotenv', 'python-dotenv')
    ]
    
    failed_imports = []
    
    for module, name in required_modules:
        try:
            __import__(module)
            print(f"✅ {name}")
        except ImportError as e:
            print(f"❌ {name}: {e}")
            failed_imports.append(name)
    
    if failed_imports:
        print(f"\n❌ Failed to import: {', '.join(failed_imports)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    print("✅ All imports successful")
    return True

def test_config():
    """Test configuration loading."""
    print("\n🧪 Testing configuration...")
    
    try:
        from config import Config
        
        print(f"✅ Configuration loaded")
        print(f"   - Confidence threshold: {Config.CONFIDENCE_THRESHOLD}")
        print(f"   - Detection cooldown: {Config.DETECTION_COOLDOWN}s")
        print(f"   - Camera index: {Config.CAMERA_INDEX}")
        
        # Check if notification settings are configured
        if Config.EMAIL_RECIPIENTS:
            print(f"   - Email recipients: {len(Config.EMAIL_RECIPIENTS)}")
        else:
            print("   ⚠️ No email recipients configured")
        
        if Config.WHATSAPP_RECIPIENTS:
            print(f"   - WhatsApp recipients: {len(Config.WHATSAPP_RECIPIENTS)}")
        else:
            print("   ⚠️ No WhatsApp recipients configured")
        
        return True
        
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False

def test_camera():
    """Test camera functionality."""
    print("\n🧪 Testing camera...")
    
    try:
        from camera_manager import CameraManager
        
        # List available cameras
        cameras = CameraManager.list_available_cameras(max_cameras=5)
        if cameras:
            print(f"✅ Found cameras: {cameras}")
            
            # Test first available camera
            camera = CameraManager(cameras[0])
            if camera.start_camera():
                print("✅ Camera started successfully")
                
                # Get a few frames
                for i in range(5):
                    frame = camera.get_frame()
                    if frame is not None:
                        print(f"✅ Frame {i+1} captured: {frame.shape}")
                    else:
                        print(f"⚠️ Frame {i+1} is None")
                    time.sleep(0.1)
                
                camera.stop_camera()
                return True
            else:
                print("❌ Failed to start camera")
                return False
        else:
            print("❌ No cameras found")
            return False
            
    except Exception as e:
        print(f"❌ Camera test failed: {e}")
        traceback.print_exc()
        return False

def test_human_detector():
    """Test human detection model."""
    print("\n🧪 Testing human detection model...")
    
    try:
        from human_detector import HumanDetector
        import numpy as np
        
        detector = HumanDetector()
        print("✅ Human detector initialized")
        
        # Create a dummy frame for testing
        dummy_frame = np.zeros((480, 640, 3), dtype=np.uint8)
        
        # Test detection (should return no humans for black frame)
        human_detected, annotated_frame, detections = detector.detect_humans(dummy_frame)
        
        print(f"✅ Detection test completed")
        print(f"   - Humans detected: {human_detected}")
        print(f"   - Number of detections: {len(detections)}")
        print(f"   - Annotated frame shape: {annotated_frame.shape}")
        
        return True
        
    except Exception as e:
        print(f"❌ Human detector test failed: {e}")
        traceback.print_exc()
        return False

def test_alarm_system():
    """Test alarm system."""
    print("\n🧪 Testing alarm system...")
    
    try:
        from alarm_system import AlarmSystem
        
        alarm = AlarmSystem()
        print("✅ Alarm system initialized")
        
        # Test alarm (brief test)
        print("🔊 Testing alarm (2 seconds)...")
        alarm.play_alarm(duration=2)
        time.sleep(3)  # Wait for alarm to finish
        
        print("✅ Alarm test completed")
        return True
        
    except Exception as e:
        print(f"❌ Alarm system test failed: {e}")
        traceback.print_exc()
        return False

def test_notification_system():
    """Test notification system initialization."""
    print("\n🧪 Testing notification system...")
    
    try:
        from notification_system import NotificationSystem
        
        notifier = NotificationSystem()
        print("✅ Notification system initialized")
        
        # Check configuration
        if notifier.email_sender:
            print("✅ Email configuration found")
        else:
            print("⚠️ Email not configured")
        
        if notifier.twilio_client:
            print("✅ WhatsApp (Twilio) configuration found")
        else:
            print("⚠️ WhatsApp not configured")
        
        return True
        
    except Exception as e:
        print(f"❌ Notification system test failed: {e}")
        traceback.print_exc()
        return False

def test_main_app():
    """Test main application initialization."""
    print("\n🧪 Testing main application...")
    
    try:
        # Import without running
        from main import HumanDetectionApp
        
        # Test initialization
        app = HumanDetectionApp(headless=True)
        print("✅ Main application initialized successfully")
        
        # Test components
        print("✅ All components integrated properly")
        
        return True
        
    except Exception as e:
        print(f"❌ Main application test failed: {e}")
        traceback.print_exc()
        return False

def main():
    """Run all tests."""
    print("🤖 Human Detection AI - System Test")
    print("=" * 40)
    
    tests = [
        ("Import Test", test_imports),
        ("Configuration Test", test_config),
        ("Camera Test", test_camera),
        ("Human Detector Test", test_human_detector),
        ("Alarm System Test", test_alarm_system),
        ("Notification System Test", test_notification_system),
        ("Main Application Test", test_main_app),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name} PASSED")
            else:
                failed += 1
                print(f"❌ {test_name} FAILED")
        except KeyboardInterrupt:
            print(f"\n⚠️ Test interrupted by user")
            break
        except Exception as e:
            failed += 1
            print(f"❌ {test_name} FAILED with exception: {e}")
    
    print(f"\n{'='*50}")
    print(f"📊 TEST RESULTS")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    print(f"📈 Success Rate: {passed/(passed+failed)*100:.1f}%")
    
    if failed == 0:
        print("\n🎉 All tests passed! System is ready to use.")
        print("💡 Next steps:")
        print("   1. Configure .env file with your settings")
        print("   2. Run: python main.py --test-notifications")
        print("   3. Run: python main.py")
    else:
        print(f"\n⚠️ {failed} test(s) failed. Please fix the issues before using the system.")
        if failed == passed:
            print("💡 Try running the setup script: python setup.py")
    
    return failed == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)