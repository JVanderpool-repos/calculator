#!/bin/bash
# DevContainer Test Script
# This script validates the DevContainer configuration

# Bash strict mode: exit on error, undefined variables, and pipe failures
set -euo pipefail

# Function to handle cleanup on exit
cleanup() {
    local exit_code=$?
    if [ $exit_code -ne 0 ]; then
        echo "❌ Test script failed with exit code $exit_code"
    fi
}

# Set trap to call cleanup function on script exit
trap cleanup EXIT

echo "🧪 Testing DevContainer Setup..."

# Test Python version
echo "📍 Python version:"
python --version

# Test pip and install requirements
echo "📦 Installing requirements..."
if ! pip install --upgrade pip -q; then
    echo "❌ Failed to upgrade pip"
    exit 1
fi

if ! pip install -r requirements.txt -q; then
    echo "❌ Failed to install production requirements"
    exit 1
fi

if ! pip install -r .devcontainer/requirements-dev.txt -q; then
    echo "❌ Failed to install development requirements"
    exit 1
fi

# Test calculator functionality
echo "🧮 Testing calculator:"
if ! python -c "from calculator import Calculator; c = Calculator(); print('Calculator test:', c.add(2, 3))"; then
    echo "❌ Calculator functionality test failed"
    exit 1
fi

# Test CLI
echo "🖥️ Testing CLI:"
if ! python main.py "sqrt(16)"; then
    echo "❌ CLI test failed"
    exit 1
fi

# Test imports
echo "🔧 Testing development tools:"
if ! python -c "import black; print('Black:', black.__version__)"; then
    echo "❌ Black import failed"
    exit 1
fi

if ! python -c "import flake8; print('Flake8:', flake8.__version__)"; then
    echo "❌ Flake8 import failed"
    exit 1
fi

if ! python -c "import mypy; print('MyPy version check skipped - no __version__ attribute')"; then
    echo "❌ MyPy import failed"
    exit 1
fi

# Test pytest
echo "🧪 Running tests:"
if ! python -m pytest tests/ -v -x --tb=short; then
    echo "❌ Pytest execution failed"
    exit 1
fi

echo "✅ DevContainer setup test completed successfully!"