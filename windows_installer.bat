@echo off
echo 🚀 Human Detection AI - Windows Installer
echo ========================================

echo 📦 Setting up Human Detection AI Security System...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found! Please install Python from https://python.org
    echo    Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo ✅ Python found

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ❌ Failed to create virtual environment
    pause
    exit /b 1
)

REM Activate virtual environment
echo 📦 Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo 📦 Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo 📦 Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Failed to install dependencies
    echo 💡 Try installing manually: pip install opencv-python ultralytics torch pygame twilio python-dotenv
    pause
    exit /b 1
)

echo ✅ Installation completed successfully!
echo.
echo 📷 Connect your webcam and test:
echo    python main.py --test-camera
echo.
echo 🚀 Run the application:
echo    python main.py
echo.
echo 📱 Don't forget to setup WhatsApp:
echo    Send "join <keyword>" to +1 415 523 8886
echo    Find keyword in your Twilio console
echo.
echo 🎉 Your AI Security System is ready!
pause