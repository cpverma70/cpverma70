#!/usr/bin/env python3
"""
Setup script for Human Detection AI Security System
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(command, description):
    """Run a system command with error handling."""
    print(f"📦 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible."""
    print("🐍 Checking Python version...")
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def install_dependencies():
    """Install Python dependencies."""
    print("📦 Installing Python dependencies...")
    
    # Upgrade pip first
    if not run_command(f"{sys.executable} -m pip install --upgrade pip", "Upgrading pip"):
        return False
    
    # Install requirements
    if not run_command(f"{sys.executable} -m pip install -r requirements.txt", "Installing dependencies"):
        return False
    
    return True

def setup_config():
    """Setup configuration file."""
    print("⚙️ Setting up configuration...")
    
    env_file = Path(".env")
    env_example = Path(".env.example")
    
    if not env_file.exists() and env_example.exists():
        shutil.copy(env_example, env_file)
        print("✅ Created .env configuration file")
        print("📝 Please edit .env file with your settings")
    else:
        print("⚠️ .env file already exists or .env.example not found")
    
    return True

def test_camera():
    """Test camera availability."""
    print("📷 Testing camera availability...")
    try:
        import cv2
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                print("✅ Default camera (index 0) is working")
                cap.release()
                return True
            else:
                print("⚠️ Camera opened but cannot read frames")
        else:
            print("⚠️ Cannot open default camera")
        cap.release()
    except ImportError:
        print("⚠️ OpenCV not installed yet, cannot test camera")
    except Exception as e:
        print(f"⚠️ Camera test failed: {e}")
    
    return False

def create_desktop_shortcut():
    """Create desktop shortcut (Linux/macOS)."""
    if sys.platform.startswith('linux') or sys.platform == 'darwin':
        print("🖥️ Creating desktop shortcut...")
        
        desktop_path = Path.home() / "Desktop"
        if desktop_path.exists():
            shortcut_content = f"""#!/bin/bash
cd "{Path.cwd()}"
python3 main.py
"""
            shortcut_file = desktop_path / "Human_Detection_AI.sh"
            with open(shortcut_file, 'w') as f:
                f.write(shortcut_content)
            
            # Make executable
            os.chmod(shortcut_file, 0o755)
            print(f"✅ Desktop shortcut created: {shortcut_file}")
        else:
            print("⚠️ Desktop folder not found")

def install_system_dependencies():
    """Install system dependencies."""
    print("🔧 Checking system dependencies...")
    
    if sys.platform.startswith('linux'):
        print("🐧 Linux detected - checking for required packages...")
        
        # Check for common dependencies
        packages_to_check = ['python3-dev', 'python3-pip', 'libgl1-mesa-glx', 'libglib2.0-0']
        missing_packages = []
        
        for package in packages_to_check:
            result = subprocess.run(['dpkg', '-l', package], capture_output=True, text=True)
            if result.returncode != 0:
                missing_packages.append(package)
        
        if missing_packages:
            print(f"⚠️ Missing packages: {', '.join(missing_packages)}")
            print("Please install them with:")
            print(f"sudo apt-get update && sudo apt-get install {' '.join(missing_packages)}")
        else:
            print("✅ All system dependencies are installed")
    
    elif sys.platform == 'darwin':
        print("🍎 macOS detected")
        print("💡 Consider installing Homebrew if you haven't already")
        print("💡 You may need: brew install portaudio")
    
    elif sys.platform.startswith('win'):
        print("🪟 Windows detected")
        print("💡 Make sure you have Visual C++ Build Tools installed")

def main():
    """Main setup function."""
    print("🤖 Human Detection AI Security System - Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install system dependencies info
    install_system_dependencies()
    
    # Install Python dependencies
    if not install_dependencies():
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    # Setup configuration
    if not setup_config():
        print("❌ Failed to setup configuration")
        sys.exit(1)
    
    # Test camera
    test_camera()
    
    # Create desktop shortcut
    create_desktop_shortcut()
    
    print("\n🎉 Setup completed successfully!")
    print("\n📝 Next steps:")
    print("1. Edit .env file with your email and WhatsApp settings")
    print("2. Test the system: python main.py --test-camera")
    print("3. Test notifications: python main.py --test-notifications")
    print("4. Run the application: python main.py")
    print("\n📖 For detailed instructions, see README.md")

if __name__ == "__main__":
    main()