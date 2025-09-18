import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # Email settings
    EMAIL_SENDER = os.getenv('EMAIL_SENDER')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
    EMAIL_RECIPIENTS = os.getenv('EMAIL_RECIPIENTS', '').split(',') if os.getenv('EMAIL_RECIPIENTS') else []
    
    # Twilio settings
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    TWILIO_WHATSAPP_FROM = os.getenv('TWILIO_WHATSAPP_FROM')
    WHATSAPP_RECIPIENTS = os.getenv('WHATSAPP_RECIPIENTS', '').split(',') if os.getenv('WHATSAPP_RECIPIENTS') else []
    
    # Detection settings
    CONFIDENCE_THRESHOLD = float(os.getenv('CONFIDENCE_THRESHOLD', 0.5))
    DETECTION_COOLDOWN = int(os.getenv('DETECTION_COOLDOWN', 10))  # seconds
    ALARM_SOUND_FILE = os.getenv('ALARM_SOUND_FILE', 'alarm.wav')
    
    # Camera settings
    CAMERA_INDEX = 0
    FRAME_WIDTH = 640
    FRAME_HEIGHT = 480