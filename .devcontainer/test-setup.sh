#!/bin/bash
# DevContainer Test Script
# This script validates the DevContainer configuration

echo "🧪 Testing DevContainer Setup..."

# Test Python version
echo "📍 Python version:"
python --version

# Test pip and install requirements
echo "📦 Installing requirements..."
pip install --upgrade pip -q
pip install -r requirements.txt -q
pip install -r .devcontainer/requirements-dev.txt -q

# Test calculator functionality
echo "🧮 Testing calculator:"
python -c "from calculator import Calculator; c = Calculator(); print('Calculator test:', c.add(2, 3))"

# Test CLI
echo "🖥️ Testing CLI:"
python main.py "sqrt(16)"

# Test imports
echo "🔧 Testing development tools:"
python -c "import black; print('Black:', black.__version__)"
python -c "import flake8; print('Flake8:', flake8.__version__)"
python -c "import mypy; print('MyPy:', mypy.__version__)"

# Test pytest
echo "🧪 Running tests:"
python -m pytest tests/ -v -x --tb=short

echo "✅ DevContainer setup test completed successfully!"