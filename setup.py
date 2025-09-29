"""
Setup configuration for the Python Calculator package.
"""

import os

from setuptools import find_packages, setup


def read_file(filename):
    """Read file contents safely."""
    try:
        with open(filename, "r", encoding="utf-8") as fh:
            return fh.read()
    except FileNotFoundError:
        return ""


def get_requirements():
    """Parse requirements.txt safely."""
    try:
        with open("requirements.txt", "r", encoding="utf-8") as fh:
            return [
                line.strip()
                for line in fh
                if line.strip() and not line.startswith("#")
            ]
    except FileNotFoundError:
        return []


long_description = read_file("README.md")
requirements = get_requirements()

setup(
    name="calculator",
    version="1.0.0",
    author="Calculator Project",
    author_email="calculator@example.com",
    description="A comprehensive Python calculator with CLI interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JVanderpool-repos/calculator",
    packages=find_packages(exclude=["tests", "tests.*"]),
    py_modules=["calculator", "main"] if not find_packages() else [],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    license="MIT",
    keywords="calculator math arithmetic cli command-line",
    python_requires=">=3.8",
    install_requires=[],  # No runtime dependencies - pure Python
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=0.990",
        ],
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "calculator=main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
