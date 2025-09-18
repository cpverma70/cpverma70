#!/usr/bin/env python3
"""
Demo script showing human detection event simulation
"""

import time
from datetime import datetime

def simulate_detection_event():
    """Simulate a human detection event."""
    
    print("🤖 Human Detection AI Security System - RUNNING")
    print("📊 [07:42:15] Monitoring... Frame: 2450, FPS: 30.0")
    print("📊 [07:42:18] Monitoring... Frame: 2540, FPS: 30.0")
    time.sleep(1)
    
    # Simulate detection event
    print()
    print("🚨" + "="*48 + "🚨")
    print("🚨 HUMAN DETECTED! Count: 1, Max Confidence: 0.87")
    print("🚨" + "="*48 + "🚨")
    
    # Sound alarm simulation
    print("🚨 HUMAN DETECTED! Playing alarm...")
    print("📢 Using console alarm (audio not available)")
    for i in range(3):
        print(f"🚨 ALERT: HUMAN DETECTED! 🚨 ({i+1}/3)")
        time.sleep(0.5)
    
    # Notification simulation
    print("\n📢 Sending notifications...")
    print("📱 Sending WhatsApp to whatsapp:+918123417647...")
    time.sleep(0.5)
    print("✅ WhatsApp sent successfully to whatsapp:+918123417647 (SID: SM1234567890)")
    
    print("📧 Sending email to cpverma1070@gmail.com...")
    time.sleep(0.5)
    print("✅ Email sent successfully to cpverma1070@gmail.com")
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    print(f"📸 Detection image saved: detection_{timestamp}.jpg")
    print("📢 Alerts sent!")
    print("=" * 50)
    
    # Cooldown simulation
    print("⏰ Cooldown active - no alerts for 10 seconds...")
    print("📊 [07:42:25] Monitoring... Frame: 2750, FPS: 30.0")
    print("📊 [07:42:28] Monitoring... Frame: 2840, FPS: 30.0")
    print("📊 [07:42:31] Monitoring... Frame: 2930, FPS: 30.0")
    
    print("\n✅ Detection event completed successfully!")
    print("💡 In a real deployment, this would:")
    print("   1. 🔊 Play actual sound alarm (if audio hardware available)")
    print("   2. 📱 Send real WhatsApp message with detection photo")
    print("   3. 📧 Send real email with detection image attachment")
    print("   4. 💾 Save detection image to disk")

if __name__ == "__main__":
    simulate_detection_event()