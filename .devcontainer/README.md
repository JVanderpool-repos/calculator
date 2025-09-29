# DevContainer Setup for Python Calculator

This directory contains the DevContainer configuration for the Python Calculator project. DevContainers provide a consistent, reproducible development environment using Docker containers.

## What's Included

### Container Configuration
- **Base Image**: Microsoft's Python 3.12 DevContainer image
- **Custom Dockerfile**: Extended with additional development tools
- **VS Code Extensions**: Pre-configured with Python development essentials

### Pre-installed Extensions
- Python language support
- Black formatter
- Flake8 linter  
- MyPy type checker
- Jupyter notebook support
- GitHub Copilot (if available)
- Test Explorer

### Development Tools
- Enhanced Python REPL (IPython)
- Jupyter notebooks
- Code quality tools (black, flake8, mypy, isort, pylint)
- Testing framework (pytest with coverage and parallel execution)
- Security scanning (bandit)
- Debugging and profiling tools
- Pre-commit hooks for code quality

## Getting Started

### Prerequisites
- Docker Desktop installed and running
- VS Code with the "Dev Containers" extension

### Opening in DevContainer
1. Open the calculator project in VS Code
2. When prompted, click "Reopen in Container"
   - Or use Command Palette: `Dev Containers: Reopen in Container`
3. Wait for the container to build and start (first time may take a few minutes)
4. The setup script (`setup.sh`) runs automatically with robust error handling
5. The development environment will be ready with all dependencies installed

### Automated Setup Process
The DevContainer uses a dedicated setup script with:
- **Error handling**: Fails fast if any dependency installation fails
- **Verification**: Confirms critical packages are properly installed
- **Logging**: Clear feedback on setup progress and any issues
- **Pre-commit hooks**: Automatically configures code quality hooks

### Manual Setup
If you prefer to build manually:
```bash
# Build the container
docker build -f .devcontainer/Dockerfile -t calculator-dev .

# Run the container
docker run -it --rm -v ${PWD}:/workspaces/calculator calculator-dev
```

## Container Features

### Environment Variables
- `PYTHONPATH=/workspaces/calculator` - Ensures proper module imports
- `PYTHONUNBUFFERED=1` - Real-time output for debugging

### Port Forwarding
- Currently no ports forwarded (can be configured for web interfaces)

### Volume Mounts
- Source code mounted at `/workspaces/calculator`
- Git directory bind-mounted for version control

## Version Management

### Centralized Configuration
All tool versions are managed centrally in `.devcontainer/versions.py`:
- **Single source of truth** for all development tool versions
- **Eliminates version drift** between requirements files and pre-commit hooks
- **Easy maintenance** - update versions in one place

### Updating Tool Versions
```bash
# Edit the central configuration
vi .devcontainer/versions.py

# Regenerate all configuration files
python .devcontainer/generate-configs.py

# Commit the updated files
git add requirements.txt .devcontainer/requirements-dev.txt .pre-commit-config.yaml
git commit -m "chore: update tool versions"
```

### Generated Files
The following files are **automatically generated** from `versions.py`:
- `requirements.txt` - Production dependencies
- `.devcontainer/requirements-dev.txt` - Development dependencies  
- `.pre-commit-config.yaml` - Pre-commit hook configuration

⚠️ **Do not edit these files directly** - changes will be overwritten!

## Development Workflow

### Running Tests
```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=calculator

# Run in parallel
pytest tests/ -n auto
```

### Code Quality
```bash
# Format code
black calculator.py main.py tests/

# Check linting
flake8 calculator.py main.py tests/

# Type checking
mypy calculator.py main.py

# Import sorting
isort calculator.py main.py tests/
```

### Interactive Development
```bash
# Enhanced Python REPL
ipython

# Start Jupyter
jupyter notebook
```

## Customization

### Adding Dependencies
Add new dependencies to:
- `requirements.txt` - Production dependencies
- `.devcontainer/requirements-dev.txt` - Development dependencies

### VS Code Settings
Modify `devcontainer.json` to customize:
- VS Code extensions
- Editor settings
- Container environment variables

### System Packages
Add system dependencies to `Dockerfile`:
```dockerfile
RUN apt-get update && apt-get install -y \
    your-package-name
```

## Benefits Over Virtual Environments

### Consistency
- Same environment across all machines
- No "works on my machine" issues
- Reproducible builds

### Isolation  
- Complete isolation from host system
- No Python version conflicts
- Clean slate for each project

### Collaboration
- Team members get identical environments
- Easy onboarding for new developers
- Consistent CI/CD pipeline

### Portability
- Works on Windows, macOS, Linux
- Cloud development ready
- Easy to share and version control

## Troubleshooting

### Container Build Issues
- Ensure Docker Desktop is running
- Check internet connectivity for package downloads
- Clear Docker cache: `docker system prune`

### Extension Issues
- Reload window: `Ctrl+Shift+P` → "Developer: Reload Window"
- Rebuild container: `Ctrl+Shift+P` → "Dev Containers: Rebuild Container"

### Permission Issues
- Container runs as `vscode` user (UID 1000)
- Files created in container are owned by this user
- Use `sudo` inside container if needed for system changes