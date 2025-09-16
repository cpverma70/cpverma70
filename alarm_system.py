import pygame
import os
import threading
import time
from config import Config

class AlarmSystem:
    def __init__(self):
        """Initialize the alarm system."""
        pygame.mixer.init()
        self.alarm_sound_file = Config.ALARM_SOUND_FILE
        self.is_playing = False
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
                
                if os.path.exists(self.alarm_sound_file) and self.alarm_sound_file.endswith('.wav'):
                    pygame.mixer.music.load(self.alarm_sound_file)
                    pygame.mixer.music.play(-1)  # Loop indefinitely
                    time.sleep(duration)
                    pygame.mixer.music.stop()
                else:
                    # Fallback: system beep
                    print("Alarm file not found, using system beep")
                    for _ in range(duration):
                        print("BEEP! HUMAN DETECTED!")
                        time.sleep(1)
                        
            except Exception as e:
                print(f"Error playing alarm: {e}")
                # Fallback to console alert
                for _ in range(duration):
                    print("🚨 ALERT: HUMAN DETECTED! 🚨")
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