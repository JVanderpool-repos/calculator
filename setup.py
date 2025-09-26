"""
Setup configuration for the Python Calculator package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="calculator",
    version="1.0.0",
    author="Calculator Project",
    author_email="calculator@example.com",
    description="A comprehensive Python calculator with CLI interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JVanderpool-repos/calculator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[],  # No runtime dependencies
    extras_require={
        "dev": requirements,
    },
    entry_points={
        "console_scripts": [
            "calculator=main:main",
        ],
    },
)