#!/bin/bash

# Human Detection AI Security System - Installation Script

echo "🤖 Human Detection AI Security System - Installation"
echo "=================================================="

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip3."
    exit 1
fi

echo "✅ pip3 found"

# Create virtual environment (optional but recommended)
read -p "🤔 Do you want to create a virtual environment? (y/N): " create_venv
if [[ $create_venv =~ ^[Yy]$ ]]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    echo "✅ Virtual environment created and activated"
fi

# Upgrade pip
echo "📦 Upgrading pip..."
pip3 install --upgrade pip

# Install requirements
echo "📦 Installing Python dependencies..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Setup configuration
if [ ! -f .env ]; then
    if [ -f .env.example ]; then
        cp .env.example .env
        echo "✅ Configuration file created (.env)"
        echo "📝 Please edit .env file with your settings"
    else
        echo "⚠️ .env.example not found"
    fi
else
    echo "⚠️ .env file already exists"
fi

# Make scripts executable
chmod +x main.py
chmod +x setup.py
chmod +x test_system.py

echo ""
echo "🎉 Installation completed!"
echo ""
echo "📝 Next steps:"
echo "1. Edit .env file with your email and WhatsApp settings"
echo "2. Test the system: python3 test_system.py"
echo "3. Run the application: python3 main.py"
echo ""
echo "💡 For detailed instructions, see README.md"

# Offer to run test
read -p "🧪 Do you want to run the system test now? (y/N): " run_test
if [[ $run_test =~ ^[Yy]$ ]]; then
    echo "🧪 Running system test..."
    python3 test_system.py
fi

echo ""
echo "🚀 Ready to use! Run 'python3 main.py' to start the human detection system."