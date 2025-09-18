#!/usr/bin/env python3
"""
Demo script to show how the Human Detection AI app would work
when running with a real camera and human detection.
"""

import time
import random
from datetime import datetime

def simulate_human_detection_app():
    """Simulate the running Human Detection AI app."""
    
    print("🤖 Human Detection AI Security System")
    print("====================================")
    print("🤖 Initializing Human Detection AI App...")
    print("Loading YOLO model...")
    print("⚠️ Audio not available: Using console alerts instead")
    print("✅ Human Detection App initialized successfully!")
    print()
    
    print("🚀 Starting Human Detection System...")
    print("📷 Camera Info: 640x480 @ 30fps")
    print("✅ System is now monitoring for humans...")
    print("📢 Notifications configured for:")
    print("   📱 WhatsApp: 1 recipients (+918123417647)")
    print("   📧 Email: 1 recipients (cpverma1070@gmail.com)")
    print()
    print("👁️ Monitoring... (Press Ctrl+C to stop)")
    print("=" * 50)
    
    frame_count = 0
    detection_count = 0
    
    try:
        while True:
            frame_count += 1
            timestamp = datetime.now().strftime("%H:%M:%S")
            
            # Simulate normal monitoring
            if frame_count % 30 == 0:  # Every 30 frames (~1 second at 30fps)
                print(f"📊 [{timestamp}] Monitoring... Frame: {frame_count}, FPS: 30.0")
            
            # Simulate human detection (randomly, about every 2-3 minutes)
            if random.randint(1, 3600) == 1:  # Very rare random detection
                detection_count += 1
                confidence = random.uniform(0.65, 0.95)
                
                print()
                print("🚨" + "="*48 + "🚨")
                print(f"🚨 HUMAN DETECTED! Count: 1, Max Confidence: {confidence:.2f}")
                print("🚨" + "="*48 + "🚨")
                
                # Simulate sound alarm
                print("🚨 HUMAN DETECTED! Playing alarm...")
                print("📢 Using console alarm (audio not available)")
                for i in range(3):
                    print(f"🚨 ALERT: HUMAN DETECTED! 🚨 ({i+1}/3)")
                    time.sleep(0.3)
                
                # Simulate notifications
                print("📢 Sending notifications...")
                print(f"📱 Sending WhatsApp to whatsapp:+918123417647...")
                print(f"📧 Sending email to cpverma1070@gmail.com...")
                print(f"Detection image saved: detection_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg")
                print("📢 Alerts sent!")
                print("=" * 50)
                
                # Simulate cooldown
                print("⏰ Cooldown active - no alerts for 10 seconds...")
                time.sleep(2)  # Shortened for demo
            
            time.sleep(0.1)  # Simulate frame processing time
            
    except KeyboardInterrupt:
        print("\n🛑 Interrupted by user")
        print("\n📊 === SESSION STATISTICS ===")
        print(f"Session Duration: {frame_count//30} seconds")
        print(f"Total Detections: {detection_count}")
        print(f"Frames Processed: {frame_count}")
        print(f"Average FPS: 30.0")
        print("✅ System stopped successfully!")

if __name__ == "__main__":
    simulate_human_detection_app()