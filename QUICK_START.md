# 🚀 **Quick Start Guide - Human Detection AI**

## 📦 **Download Package**

You have a complete deployment package: `human_detection_ai_complete.tar.gz`

This contains everything you need:
- ✅ All Python files pre-configured
- ✅ Your email and WhatsApp settings already set
- ✅ Installation scripts for all platforms
- ✅ Complete documentation

---

## 🖥️ **Choose Your Operating System**

### **🐧 Linux (Ubuntu/Debian)**

```bash
# 1. Extract files
tar -xzf human_detection_ai_complete.tar.gz
cd human_detection_ai

# 2. Install system dependencies
sudo apt update
sudo apt install python3-venv python3-pip python3-dev

# 3. Run auto-installer
chmod +x install.sh
./install.sh

# 4. Connect webcam and test
source venv/bin/activate
python3 main.py --test-camera

# 5. Run the application
python3 main.py
```

### **🍎 macOS**

```bash
# 1. Extract files
tar -xzf human_detection_ai_complete.tar.gz
cd human_detection_ai

# 2. Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 3. Install Python
brew install python3

# 4. Run auto-installer
chmod +x install.sh
./install.sh

# 5. Connect webcam and test
source venv/bin/activate
python3 main.py --test-camera

# 6. Run the application
python3 main.py
```

### **🪟 Windows**

```cmd
# 1. Extract files using WinRAR/7-Zip to: C:\human_detection_ai
# 2. Open Command Prompt as Administrator
cd C:\human_detection_ai

# 3. Install Python (if not installed)
# Download from: https://www.python.org/downloads/

# 4. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 5. Install dependencies
pip install -r requirements.txt

# 6. Connect webcam and test
python main.py --test-camera

# 7. Run the application
python main.py
```

---

## 📷 **Camera Setup**

### **Connect Your Camera:**
- Built-in laptop webcam ✅
- USB webcam ✅
- External camera ✅

### **Test Camera:**
```bash
# List available cameras
python3 main.py --list-cameras

# Test camera 0 (usually default)
python3 main.py --test-camera --camera 0

# Try camera 1 if 0 doesn't work
python3 main.py --test-camera --camera 1
```

---

## 📱 **WhatsApp Setup (Required)**

Your Twilio is configured, but you need to connect your phone:

1. **Send WhatsApp to:** `+1 415 523 8886`
2. **Message:** `join <keyword>`
3. **Find keyword:** [Twilio Console](https://console.twilio.com) → Messaging → WhatsApp

---

## 🚀 **Run the Application**

### **With Live Camera Display:**
```bash
python3 main.py
```
- Shows live video feed
- Real-time detection overlay
- Press 'q' to quit

### **Background Mode (No Display):**
```bash
python3 main.py --headless
```
- Runs silently in background
- Perfect for 24/7 monitoring
- Lower resource usage

---

## 🚨 **What Happens When Human Detected**

1. **🔊 SOUND ALARM** - Immediate audio alert
2. **📧 EMAIL ALERT** → `cpverma1070@gmail.com` with detection photo
3. **📱 WHATSAPP MESSAGE** → `+918123417647` with detection image
4. **📸 PHOTO SAVED** - Detection image saved locally
5. **⏰ COOLDOWN** - 10 seconds before next alert

---

## ⚡ **One-Command Installation**

### **Linux/macOS:**
```bash
# Extract and run in one go
tar -xzf human_detection_ai_complete.tar.gz && cd human_detection_ai && chmod +x install.sh && ./install.sh
```

### **Windows PowerShell:**
```powershell
# Extract files first, then:
cd human_detection_ai; python -m venv venv; venv\Scripts\activate; pip install -r requirements.txt
```

---

## 🛠️ **Troubleshooting**

### **Camera Not Working:**
```bash
# Check camera permissions (Linux)
sudo usermod -a -G video $USER
# Logout and login again

# Try different camera index
python3 main.py --camera 1
python3 main.py --camera 2
```

### **Email Not Working:**
- Use Gmail App Password instead of regular password
- Go to Google Account → Security → App passwords
- Replace password in `.env` file

### **Dependencies Failed:**
```bash
# Update pip first
pip install --upgrade pip

# Install one by one if batch fails
pip install opencv-python ultralytics torch pygame twilio python-dotenv
```

---

## 📊 **System Test**

Before running, test everything:
```bash
python3 test_system.py
```

This checks:
- ✅ All imports working
- ✅ Configuration loaded
- ✅ Camera detection
- ✅ AI model ready
- ✅ Notifications configured

---

## 🎯 **Performance Tips**

### **Better Detection:**
- Good lighting conditions
- Camera at eye level
- Stable internet for notifications

### **Lower Resource Usage:**
- Run headless: `python3 main.py --headless`
- Increase cooldown: Edit `DETECTION_COOLDOWN=30` in `.env`
- Close other camera apps

---

## 🔐 **Security Notes**

- Your credentials are in `.env` file - keep it secure
- Email uses encrypted connection
- WhatsApp uses Twilio's secure API
- All AI processing is local (no cloud)

---

## 🎉 **You're Ready!**

Your Human Detection AI Security System includes:

- ✅ **Real-time AI human detection** using YOLOv8
- ✅ **Multi-channel alerts** (sound + email + WhatsApp)
- ✅ **Smart cooldown** prevents notification spam
- ✅ **Photo capture** of every detection
- ✅ **24/7 monitoring** capability
- ✅ **Professional security system**

**Connect your camera and start protecting your space with AI! 🛡️🚀**

---

## 📞 **Support**

If you need help:
1. Run `python3 test_system.py` for diagnostics
2. Check `README.md` for detailed documentation
3. Test components individually with `--test-*` flags

**Your AI security system is ready to deploy! 🎯**