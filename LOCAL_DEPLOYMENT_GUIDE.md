# 🚀 **Deploy Human Detection AI on Your Local Machine**

## 📁 **Files You Need to Copy**

Copy these files to your local machine:

### **Core Application Files:**
- `main.py` - Main application
- `human_detector.py` - AI detection engine  
- `camera_manager.py` - Camera handling
- `alarm_system.py` - Sound alerts
- `notification_system.py` - Email & WhatsApp
- `config.py` - Configuration loader

### **Configuration Files:**
- `.env` - Your configured settings ✅
- `.env.example` - Template file
- `requirements.txt` - Dependencies

### **Setup & Testing:**
- `install.sh` - Auto installer (Linux/macOS)
- `setup.py` - Python setup script
- `test_system.py` - System tester
- `README.md` - Full documentation

---

## 🖥️ **Installation on Your Local Machine**

### **Option 1: Linux/macOS (Recommended)**
```bash
# 1. Copy files to your local directory
cd ~/Desktop
mkdir human_detection_ai
cd human_detection_ai

# 2. Copy all files here, then:
chmod +x install.sh
./install.sh

# 3. Connect your webcam and run:
source venv/bin/activate
python3 main.py --test-camera
python3 main.py
```

### **Option 2: Windows**
```cmd
# 1. Copy files to your local directory
cd C:\Users\YourName\Desktop
mkdir human_detection_ai
cd human_detection_ai

# 2. Copy all files here, then:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# 3. Connect your webcam and run:
python main.py --test-camera
python main.py
```

### **Option 3: Manual Python Setup**
```bash
# 1. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# OR
venv\Scripts\activate     # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Test and run
python3 main.py --test-camera
python3 main.py
```

---

## 📷 **Camera Requirements**

### **Supported Cameras:**
- ✅ Built-in laptop webcam
- ✅ USB webcams
- ✅ External USB cameras
- ✅ Most UVC-compatible cameras

### **Test Your Camera:**
```bash
# Check available cameras
python3 main.py --list-cameras

# Test specific camera
python3 main.py --test-camera --camera 0
python3 main.py --test-camera --camera 1
```

---

## 🔧 **Your Pre-Configured Settings**

Your system is already configured with:

```env
# Email Settings
EMAIL_SENDER=awadhdarsan@gmail.com
EMAIL_PASSWORD=Chandra@102
EMAIL_RECIPIENTS=cpverma1070@gmail.com

# WhatsApp Settings (Twilio)
TWILIO_ACCOUNT_SID=US56d596da942a86b674155316b0b75b9d
TWILIO_AUTH_TOKEN=85175f0fe437d8761ba5390889ea58f3
WHATSAPP_RECIPIENTS=whatsapp:+918123417647

# Detection Settings
CONFIDENCE_THRESHOLD=0.5
DETECTION_COOLDOWN=10
```

---

## 📱 **WhatsApp Setup (Required)**

Before WhatsApp works, connect your phone:

1. **Send WhatsApp message to:** `+1 415 523 8886`
2. **Message content:** `join <sandbox-keyword>`
3. **Find your keyword:** Login to Twilio Console → Messaging → WhatsApp

---

## 🚀 **Running the Application**

### **Interactive Mode (with GUI):**
```bash
python3 main.py
```
- Shows live camera feed
- Real-time detection overlay
- Press 'q' to quit, 's' for stats, 't' to test

### **Background Mode (no GUI):**
```bash
python3 main.py --headless
```
- Runs in background
- Perfect for always-on monitoring
- Lower resource usage

### **Testing Commands:**
```bash
# Test camera
python3 main.py --test-camera

# Test notifications
python3 main.py --test-notifications

# Test alarm
python3 main.py --test-alarm

# List cameras
python3 main.py --list-cameras

# Full system test
python3 test_system.py
```

---

## 🚨 **What Happens When Human Detected**

1. **🔊 Sound Alarm** - Immediate audio alert
2. **📧 Email Alert** - Sent to `cpverma1070@gmail.com` with photo
3. **📱 WhatsApp Message** - Sent to `+918123417647` with image
4. **📸 Image Saved** - Detection photo saved locally
5. **⏰ Cooldown** - 10 seconds before next alert

---

## 🛠️ **Troubleshooting**

### **Camera Issues:**
```bash
# Check if camera is in use
lsof /dev/video0  # Linux
# Close other apps using camera

# Try different camera index
python3 main.py --camera 1
python3 main.py --camera 2
```

### **Permission Issues (Linux):**
```bash
# Add user to video group
sudo usermod -a -G video $USER
# Logout and login again
```

### **Email Issues:**
- Use Gmail App Password instead of regular password
- Enable 2-Factor Authentication first
- Test with: `python3 main.py --test-notifications`

---

## 🎯 **Performance Tips**

### **For Better Performance:**
- Use wired internet connection
- Close unnecessary applications
- Use dedicated USB camera (better than built-in)
- Run in headless mode: `python3 main.py --headless`

### **For Lower-End Systems:**
- Reduce confidence threshold: `CONFIDENCE_THRESHOLD=0.3`
- Increase cooldown: `DETECTION_COOLDOWN=30`
- Use smaller camera resolution in `config.py`

---

## 🎉 **Ready to Protect Your Space!**

Your Human Detection AI Security System is ready to deploy! Once you copy the files and connect a camera, you'll have:

- ✅ **Real-time AI human detection**
- ✅ **Multi-channel alerts** (sound, email, WhatsApp)  
- ✅ **Smart cooldown** to prevent spam
- ✅ **Detection photos** automatically saved
- ✅ **Professional security monitoring**

**Deploy it now and start protecting your space with AI! 🛡️🚀**