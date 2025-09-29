#!/usr/bin/env python3
"""
Generate requirements files from centralized version configuration.
This ensures consistency between requirements.txt, requirements-dev.txt, and pre-commit config.
"""

import os
import sys
from pathlib import Path

# Add the .devcontainer directory to Python path to import versions
sys.path.insert(0, str(Path(__file__).parent))

try:
    from versions import *
except ImportError:
    print("❌ Error: Could not import versions.py")
    print("Make sure versions.py exists in the .devcontainer directory")
    sys.exit(1)


def generate_requirements_txt():
    """Generate the main requirements.txt file."""
    content = f"""# Python Calculator Requirements
# 
# ⚠️  AUTO-GENERATED FILE - DO NOT EDIT DIRECTLY
# This file is generated from .devcontainer/versions.py
# To update versions, edit versions.py and run: python .devcontainer/generate-configs.py
# 
# Production dependencies
setuptools>=65.0.0
wheel>=0.37.0

# Development and testing dependencies
pytest>={PYTEST_VERSION}
pytest-cov>={PYTEST_COV_VERSION}

# Code quality tools
black=={BLACK_VERSION}  # Match pre-commit hook version
flake8=={FLAKE8_VERSION}  # Match pre-commit hook version
mypy>={MYPY_VERSION}

# Documentation
sphinx>={SPHINX_VERSION}
sphinx-rtd-theme>={SPHINX_RTD_THEME_VERSION}
"""
    return content


def generate_requirements_dev_txt():
    """Generate the development requirements file."""
    content = f"""# Development Container Requirements
# Extended requirements for the development environment
# 
# ⚠️  AUTO-GENERATED FILE - DO NOT EDIT DIRECTLY
# This file is generated from .devcontainer/versions.py
# To update versions, edit versions.py and run: python .devcontainer/generate-configs.py

# Base requirements (from requirements.txt)
setuptools>=65.0.0
wheel>=0.37.0

# Testing framework
pytest>={PYTEST_VERSION}
pytest-cov>={PYTEST_COV_VERSION}
pytest-xdist>={PYTEST_XDIST_VERSION}  # Parallel test execution

# Code quality and formatting
black=={BLACK_VERSION}  # Match pre-commit hook version
flake8=={FLAKE8_VERSION}  # Match pre-commit hook version
mypy>={MYPY_VERSION}
isort=={ISORT_VERSION}  # Match pre-commit hook version
pylint>={PYLINT_VERSION}  # Additional linting

# Documentation
sphinx>={SPHINX_VERSION}
sphinx-rtd-theme>={SPHINX_RTD_THEME_VERSION}

# Development tools
ipython>={IPYTHON_VERSION}  # Enhanced Python REPL
jupyter>={JUPYTER_VERSION}  # Notebook support
pre-commit>={PRE_COMMIT_VERSION}  # Git hooks for code quality
bandit=={BANDIT_VERSION}  # Match pre-commit hook version

# Debugging and profiling
pdbpp>={PDBPP_VERSION}  # Enhanced debugger (pdb++)
memory-profiler>={MEMORY_PROFILER_VERSION}  # Memory profiling
line-profiler>={LINE_PROFILER_VERSION}  # Line-by-line profiling
"""
    return content


def generate_precommit_config():
    """Generate the pre-commit configuration with version references."""
    content = f"""# Pre-commit hooks for code quality
# Install with: pre-commit install
# Run on all files: pre-commit run --all-files
# 
# ⚠️  AUTO-GENERATED FILE - DO NOT EDIT DIRECTLY
# This file is generated from .devcontainer/versions.py
# To update versions, edit versions.py and run: python .devcontainer/generate-configs.py
# 
# Versions are managed centrally in .devcontainer/versions.py

repos:
  # Code formatting
  - repo: https://github.com/psf/black
    rev: {BLACK_VERSION}
    hooks:
      - id: black
        language_version: python3
        args: [--line-length=127]

  # Import sorting
  - repo: https://github.com/pycqa/isort
    rev: {ISORT_VERSION}
    hooks:
      - id: isort
        args: [--profile=black, --line-length=127]

  # Linting
  - repo: https://github.com/pycqa/flake8
    rev: {FLAKE8_VERSION}
    hooks:
      - id: flake8
        args: [--max-line-length=127, --extend-ignore=E203,W503]

  # Security scanning
  - repo: https://github.com/pycqa/bandit
    rev: {BANDIT_VERSION}
    hooks:
      - id: bandit
        args: ['-c', '.bandit.yml']
        exclude: tests/

  # General file cleanup
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: {PRE_COMMIT_HOOKS_VERSION}
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json
      - id: check-merge-conflict
      - id: check-added-large-files
"""
    return content


def main():
    """Generate all configuration files from the central version source."""
    project_root = Path(__file__).parent.parent
    devcontainer_dir = Path(__file__).parent

    print("🔧 Generating configuration files from centralized versions...")

    # Generate requirements.txt
    requirements_path = project_root / "requirements.txt"
    print(f"📝 Generating {requirements_path}")
    with open(requirements_path, "w", encoding="utf-8") as f:
        f.write(generate_requirements_txt())

    # Generate requirements-dev.txt
    requirements_dev_path = devcontainer_dir / "requirements-dev.txt"
    print(f"📝 Generating {requirements_dev_path}")
    with open(requirements_dev_path, "w", encoding="utf-8") as f:
        f.write(generate_requirements_dev_txt())

    # Generate .pre-commit-config.yaml
    precommit_path = project_root / ".pre-commit-config.yaml"
    print(f"📝 Generating {precommit_path}")
    with open(precommit_path, "w", encoding="utf-8") as f:
        f.write(generate_precommit_config())

    print("✅ All configuration files generated successfully!")
    print(
        "💡 To update versions, edit .devcontainer/versions.py and run this script again"
    )


if __name__ == "__main__":
    main()
