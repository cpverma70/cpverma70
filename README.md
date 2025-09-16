# 🤖 Human Detection AI Security System

A comprehensive AI-powered security system that detects humans in real-time using computer vision and sends instant alerts via sound alarms, WhatsApp, and email notifications.

## ✨ Features

- **🎯 Real-time Human Detection**: Uses YOLOv8 AI model for accurate human detection
- **🔊 Sound Alarms**: Immediate audio alerts when humans are detected
- **📱 WhatsApp Notifications**: Instant WhatsApp messages with detection images
- **📧 Email Alerts**: Email notifications with timestamped detection photos
- **📷 Multi-camera Support**: Works with webcams, USB cameras, and IP cameras
- **⚙️ Configurable Settings**: Customizable detection sensitivity and cooldown periods
- **📊 Real-time Statistics**: Live monitoring dashboard with detection metrics
- **🚫 Smart Cooldown**: Prevents spam notifications with configurable intervals

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Install Python dependencies
pip install -r requirements.txt

# For audio support (Linux)
sudo apt-get install python3-pygame

# For audio support (macOS)
brew install portaudio
```

### 2. Configure Settings

```bash
# Copy example configuration
cp .env.example .env

# Edit configuration file
nano .env
```

Configure your settings in `.env`:

```env
# Email Configuration (Gmail)
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECIPIENTS=recipient1@gmail.com,recipient2@gmail.com

# Twilio Configuration (for WhatsApp)
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_WHATSAPP_FROM=whatsapp:+14155238886
WHATSAPP_RECIPIENTS=whatsapp:+1234567890,whatsapp:+0987654321

# Detection Settings
CONFIDENCE_THRESHOLD=0.5
DETECTION_COOLDOWN=10
```

### 3. Run the Application

```bash
# Basic usage
python main.py

# Headless mode (no GUI)
python main.py --headless

# Specify camera
python main.py --camera 0

# Test systems
python main.py --test-camera
python main.py --test-notifications
python main.py --list-cameras
```

## 📋 Setup Instructions

### Email Setup (Gmail)

1. Enable 2-Factor Authentication on your Gmail account
2. Generate an App Password:
   - Go to Google Account settings
   - Security → App passwords
   - Generate password for "Mail"
3. Use the generated password in `EMAIL_PASSWORD`

### WhatsApp Setup (Twilio)

1. Create a Twilio account at [twilio.com](https://www.twilio.com)
2. Get your Account SID and Auth Token from the dashboard
3. Enable WhatsApp sandbox or get approved for production
4. Configure phone numbers in international format: `whatsapp:+1234567890`

### Camera Setup

- **Webcam**: Usually camera index 0
- **USB Camera**: Try indices 1, 2, etc.
- **IP Camera**: Use RTSP URL as camera source (requires code modification)

## 🎮 Usage

### Interactive Mode (Default)

```bash
python main.py
```

**Controls:**
- `q`: Quit application
- `s`: Show statistics
- `t`: Test notifications

### Headless Mode (Background)

```bash
python main.py --headless
```

Perfect for running as a service or on headless systems.

### Command Line Options

```bash
python main.py --help
```

Available options:
- `--camera INDEX`: Specify camera index
- `--headless`: Run without GUI
- `--test-camera`: Test camera functionality
- `--list-cameras`: List available cameras
- `--test-notifications`: Test notification systems
- `--test-alarm`: Test alarm system

## 🔧 Configuration Options

### Detection Settings

| Setting | Description | Default |
|---------|-------------|---------|
| `CONFIDENCE_THRESHOLD` | Minimum detection confidence (0.0-1.0) | 0.5 |
| `DETECTION_COOLDOWN` | Seconds between notifications | 10 |
| `CAMERA_INDEX` | Default camera to use | 0 |
| `FRAME_WIDTH` | Camera frame width | 640 |
| `FRAME_HEIGHT` | Camera frame height | 480 |

### Notification Settings

- **Email Recipients**: Comma-separated list of email addresses
- **WhatsApp Recipients**: Comma-separated list in format `whatsapp:+1234567890`
- **Alarm Sound**: Path to custom `.wav` file (optional)

## 📊 System Requirements

- **Python**: 3.7+
- **Camera**: Webcam, USB camera, or IP camera
- **RAM**: 2GB minimum, 4GB recommended
- **CPU**: Multi-core processor recommended
- **Internet**: Required for notifications and model download

### Supported Platforms

- ✅ Linux (Ubuntu, Debian, CentOS)
- ✅ macOS (10.14+)
- ✅ Windows 10/11
- ✅ Raspberry Pi (4GB+ recommended)

## 🛠️ Troubleshooting

### Common Issues

**Camera not found:**
```bash
# List available cameras
python main.py --list-cameras

# Test specific camera
python main.py --test-camera --camera 1
```

**Email not working:**
- Check Gmail App Password setup
- Verify email credentials in `.env`
- Test with: `python main.py --test-notifications`

**WhatsApp not working:**
- Verify Twilio credentials
- Check phone number format: `whatsapp:+1234567890`
- Ensure WhatsApp sandbox is active

**Low detection accuracy:**
- Increase `CONFIDENCE_THRESHOLD` for fewer false positives
- Decrease for more sensitive detection
- Ensure good lighting conditions

**Performance issues:**
- Reduce camera resolution in `config.py`
- Use `--headless` mode for better performance
- Close other applications using the camera

### Logs and Debugging

The application provides detailed console output for debugging:
- Detection events with confidence scores
- Notification delivery status
- Camera and system information
- Error messages with suggestions

## 🔒 Security & Privacy

- **Local Processing**: All AI detection runs locally on your device
- **No Cloud Storage**: Images are only sent via your configured notifications
- **Temporary Files**: Detection images are automatically cleaned up
- **Encrypted Communications**: Email and WhatsApp use encrypted channels

## 📈 Performance Optimization

### For High Performance:
- Use dedicated GPU (CUDA support available)
- Increase camera resolution for better detection
- Use wired network connection for notifications

### For Low-End Systems:
- Use `--headless` mode
- Reduce camera resolution
- Increase `DETECTION_COOLDOWN` to reduce processing

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Additional notification channels (Slack, Discord, etc.)
- Web dashboard interface
- Mobile app integration
- Advanced detection filters
- Multi-camera support

## 📄 License

MIT License - see LICENSE file for details.

## 🆘 Support

For issues and questions:
1. Check the troubleshooting section above
2. Review console output for error messages
3. Test individual components using the test commands
4. Ensure all dependencies are properly installed

---

**⚠️ Important Notes:**
- This system is for security monitoring purposes
- Ensure compliance with local privacy laws
- Test thoroughly before deploying in production
- Keep your notification credentials secure