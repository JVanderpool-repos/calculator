#!/bin/bash
# DevContainer Setup Script
# This script handles the post-creation setup of the DevContainer environment
#
# Tool versions are managed centrally in versions.py
# Use generate-configs.py to regenerate requirements and pre-commit config

# Bash strict mode: exit on error, undefined variables, and pipe failures
set -euo pipefail

echo "🚀 Setting up DevContainer environment..."

# Function to handle cleanup on exit
cleanup() {
    local exit_code=$?
    if [ $exit_code -ne 0 ]; then
        echo "❌ DevContainer setup failed with exit code $exit_code"
        echo "💡 Check the logs above for specific error details"
    else
        echo "✅ DevContainer setup completed successfully!"
    fi
}

# Set trap to call cleanup function on script exit
trap cleanup EXIT

# Upgrade pip with error handling
echo "📦 Upgrading pip..."
if ! pip install --upgrade pip; then
    echo "❌ Failed to upgrade pip"
    exit 1
fi

# Install production dependencies
echo "📦 Installing production requirements..."
if ! pip install -r requirements.txt; then
    echo "❌ Failed to install production requirements from requirements.txt"
    echo "💡 Check if requirements.txt exists and contains valid package specifications"
    exit 1
fi

# Install development dependencies
echo "📦 Installing development requirements..."
if ! pip install -r .devcontainer/requirements-dev.txt; then
    echo "❌ Failed to install development requirements from .devcontainer/requirements-dev.txt"
    echo "💡 Check if .devcontainer/requirements-dev.txt exists and contains valid package specifications"
    exit 1
fi

# Verify critical packages are installed
echo "🔍 Verifying installation..."
critical_packages=("pytest" "black" "flake8" "mypy")

for package in "${critical_packages[@]}"; do
    if ! python -c "import $package" 2>/dev/null; then
        echo "❌ Critical package '$package' not found after installation"
        exit 1
    fi
done

echo "🎉 All critical packages verified successfully!"

# Set up pre-commit hooks (optional, non-failing)
echo "🪝 Setting up pre-commit hooks..."
if command -v pre-commit >/dev/null 2>&1; then
    if pre-commit install; then
        echo "✅ Pre-commit hooks installed successfully"
    else
        echo "⚠️  Warning: Failed to install pre-commit hooks (non-critical)"
    fi
else
    echo "⚠️  Warning: pre-commit not available (non-critical)"
fi

echo "🎯 DevContainer setup phase completed!"