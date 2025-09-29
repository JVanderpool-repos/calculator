"""
Python Calculator Package

A comprehensive calculator implementation with CLI and GUI interfaces.
Features both command-line and graphical user interface modes.
"""

from .calculator import Calculator, add, divide, multiply, subtract

# GUI import is optional to handle environments without tkinter
try:
    from .calculator_gui import CalculatorGUI  # noqa: F401

    __all__ = ["Calculator", "CalculatorGUI", "add", "subtract", "multiply", "divide"]
except ImportError:
    # GUI not available (e.g., headless environment)
    __all__ = ["Calculator", "add", "subtract", "multiply", "divide"]

__version__ = "1.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"
