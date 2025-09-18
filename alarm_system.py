import pygame
import os
import threading
import time
from config import Config

class AlarmSystem:
    def __init__(self):
        """Initialize the alarm system."""
        self.alarm_sound_file = Config.ALARM_SOUND_FILE
        self.is_playing = False
        self.audio_available = False
        
        # Try to initialize pygame mixer
        try:
            pygame.mixer.init()
            self.audio_available = True
            print("✅ Audio system initialized")
        except pygame.error as e:
            print(f"⚠️ Audio not available: {e}")
            print("📢 Will use console alerts instead")
            self.audio_available = False
        
        if self.audio_available:
            self._create_default_alarm_sound()
        
    def _create_default_alarm_sound(self):
        """Create a default alarm sound if none exists."""
        if not os.path.exists(self.alarm_sound_file):
            print(f"Creating default alarm sound: {self.alarm_sound_file}")
            # Generate a simple beep sound
            import numpy as np
            from scipy.io.wavfile import write
            
            try:
                # Generate a 2-second alarm sound
                sample_rate = 44100
                duration = 2.0
                frequency = 1000  # 1kHz beep
                
                t = np.linspace(0, duration, int(sample_rate * duration), False)
                # Create a beeping pattern
                wave = np.sin(frequency * 2 * np.pi * t) * np.sin(10 * 2 * np.pi * t)
                wave = (wave * 32767).astype(np.int16)
                
                write(self.alarm_sound_file, sample_rate, wave)
                print(f"Default alarm sound created: {self.alarm_sound_file}")
            except ImportError:
                print("scipy not available, creating simple alarm file placeholder")
                # Create a placeholder file
                with open(self.alarm_sound_file, 'w') as f:
                    f.write("# Placeholder alarm file - replace with actual .wav file")
    
    def play_alarm(self, duration=5):
        """
        Play alarm sound for specified duration.
        
        Args:
            duration: Duration to play alarm in seconds
        """
        if self.is_playing:
            return
            
        def _play():
            try:
                self.is_playing = True
                print("🚨 HUMAN DETECTED! Playing alarm...")
                
                if self.audio_available and os.path.exists(self.alarm_sound_file) and self.alarm_sound_file.endswith('.wav'):
                    pygame.mixer.music.load(self.alarm_sound_file)
                    pygame.mixer.music.play(-1)  # Loop indefinitely
                    time.sleep(duration)
                    pygame.mixer.music.stop()
                else:
                    # Fallback: console alert with visual emphasis
                    print("📢 Using console alarm (audio not available)")
                    for i in range(duration):
                        print(f"🚨 ALERT: HUMAN DETECTED! 🚨 ({i+1}/{duration})")
                        time.sleep(1)
                        
            except Exception as e:
                print(f"Error playing alarm: {e}")
                # Fallback to console alert
                for i in range(duration):
                    print(f"🚨 ALERT: HUMAN DETECTED! 🚨 ({i+1}/{duration})")
                    time.sleep(1)
            finally:
                self.is_playing = False
        
        # Play alarm in separate thread to avoid blocking
        alarm_thread = threading.Thread(target=_play)
        alarm_thread.daemon = True
        alarm_thread.start()
    
    def stop_alarm(self):
        """Stop the currently playing alarm."""
        try:
            if self.audio_available:
                pygame.mixer.music.stop()
            self.is_playing = False
            print("Alarm stopped")
        except Exception as e:
            print(f"Error stopping alarm: {e}")
    
    def test_alarm(self):
        """Test the alarm system."""
        print("Testing alarm system...")
        self.play_alarm(duration=2)
        time.sleep(3)
        print("Alarm test completed")