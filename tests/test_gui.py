"""
Unit tests for the Calculator GUI.

This module contains tests for the GUI calculator functionality,
focusing on integration with the Calculator class and state management.
Note: These tests mock the GUI components to avoid requiring a display.
"""

import tkinter as tk
import unittest
from unittest.mock import Mock, patch

from calculator_gui import CalculatorGUI


class TestCalculatorGUI(unittest.TestCase):
    """Test cases for the Calculator GUI class."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        # Mock tkinter to avoid needing a display
        self.mock_root = Mock(spec=tk.Tk)

        # Configure mock return values for screen methods
        self.mock_root.winfo_screenwidth.return_value = 1920
        self.mock_root.winfo_screenheight.return_value = 1080

        with patch("calculator_gui.tk.Tk"), patch(
            "calculator_gui.ttk.Frame"
        ), patch("calculator_gui.ttk.LabelFrame"), patch(
            "calculator_gui.ttk.Entry"
        ), patch(
            "calculator_gui.ttk.Button"
        ), patch(
            "calculator_gui.ttk.Style"
        ), patch(
            "calculator_gui.tk.StringVar"
        ) as mock_stringvar:
            # Mock StringVar
            mock_stringvar.return_value = Mock()

            self.gui = CalculatorGUI(self.mock_root)

    def test_initialization(self):
        """Test GUI initialization."""
        self.assertIsNotNone(self.gui.calculator)
        self.assertEqual(self.gui.current_input, "")
        self.assertIsNone(self.gui.pending_operation)
        self.assertIsNone(self.gui.pending_value)
        self.assertFalse(self.gui.just_calculated)

    def test_number_input(self):
        """Test number button functionality."""
        # Test single digit
        self.gui.number("5")
        self.assertEqual(self.gui.current_input, "5")

        # Test multiple digits
        self.gui.number("3")
        self.assertEqual(self.gui.current_input, "53")

        # Test replacing zero
        self.gui.current_input = "0"
        self.gui.number("7")
        self.assertEqual(self.gui.current_input, "7")

    def test_decimal_input(self):
        """Test decimal point functionality."""
        # Test adding decimal to empty input
        self.gui.decimal()
        self.assertEqual(self.gui.current_input, "0.")

        # Test adding decimal to existing number
        self.gui.current_input = "5"
        self.gui.decimal()
        self.assertEqual(self.gui.current_input, "5.")

        # Test preventing multiple decimals
        self.gui.decimal()
        self.assertEqual(self.gui.current_input, "5.")  # Should not change

    def test_clear_functions(self):
        """Test clear and clear entry functions."""
        # Set up some state
        self.gui.current_input = "123"
        self.gui.pending_operation = "+"
        self.gui.pending_value = 45.0
        self.gui.just_calculated = True

        # Test clear entry
        self.gui.clear_entry()
        self.assertEqual(self.gui.current_input, "")
        self.assertEqual(self.gui.pending_operation, "+")  # Should remain

        # Test full clear
        self.gui.clear()
        self.assertEqual(self.gui.current_input, "")
        self.assertIsNone(self.gui.pending_operation)
        self.assertIsNone(self.gui.pending_value)
        self.assertFalse(self.gui.just_calculated)

    def test_backspace(self):
        """Test backspace functionality."""
        self.gui.current_input = "123"
        self.gui.backspace()
        self.assertEqual(self.gui.current_input, "12")

        self.gui.backspace()
        self.assertEqual(self.gui.current_input, "1")

        self.gui.backspace()
        self.assertEqual(self.gui.current_input, "")

    def test_toggle_sign(self):
        """Test sign toggle functionality."""
        self.gui.current_input = "123"
        self.gui.toggle_sign()
        self.assertEqual(self.gui.current_input, "-123")

        self.gui.toggle_sign()
        self.assertEqual(self.gui.current_input, "123")

    def test_basic_operations(self):
        """Test basic arithmetic operations."""
        # Test addition
        self.gui.current_input = "5"
        self.gui.operation("+")
        self.assertEqual(self.gui.pending_operation, "+")
        self.assertEqual(self.gui.pending_value, 5.0)

        self.gui.current_input = "3"
        self.gui.equals()
        self.assertEqual(self.gui.current_input, "8.0")
        self.assertTrue(self.gui.just_calculated)

    def test_advanced_operations(self):
        """Test advanced mathematical operations."""
        # Test square root
        self.gui.current_input = "25"
        self.gui.square_root()
        self.assertEqual(self.gui.current_input, "5.0")
        self.assertTrue(self.gui.just_calculated)

        # Test square
        self.gui.current_input = "4"
        self.gui.square()
        self.assertEqual(self.gui.current_input, "16.0")

        # Test percentage
        self.gui.current_input = "50"
        self.gui.percentage()
        self.assertEqual(self.gui.current_input, "0.5")

    def test_trigonometric_functions(self):
        """Test trigonometric functions."""
        # Test sine
        self.gui.current_input = "90"
        self.gui.sine()
        # Should be approximately 1.0
        result = float(self.gui.current_input)
        self.assertAlmostEqual(result, 1.0, places=10)

        # Test cosine
        self.gui.current_input = "0"
        self.gui.cosine()
        result = float(self.gui.current_input)
        self.assertAlmostEqual(result, 1.0, places=10)

    def test_factorial(self):
        """Test factorial operation."""
        self.gui.current_input = "5"
        self.gui.factorial()
        self.assertEqual(self.gui.current_input, "120")

    def test_error_handling(self):
        """Test error handling for invalid operations."""
        # Test square root of negative number
        self.gui.current_input = "-1"
        with patch.object(self.gui, "show_error") as mock_error:
            self.gui.square_root()
            mock_error.assert_called()

    def test_display_updates(self):
        """Test display update functionality."""
        with patch.object(self.gui, "display_var") as mock_display:
            # Test normal number display
            self.gui.update_display("123.45")
            mock_display.set.assert_called_with("123.45")

            # Test very long number (scientific notation)
            long_number = "1" * 25
            self.gui.update_display(long_number)
            # Should call set with a truncated or scientific notation
            mock_display.set.assert_called()

    def test_calculation_chain(self):
        """Test chaining multiple calculations."""
        # 5 + 3 * 2 = 16 (if calculated left to right)
        self.gui.current_input = "5"
        self.gui.operation("+")
        self.gui.current_input = "3"
        self.gui.operation("*")  # Should trigger equals first
        self.gui.current_input = "2"
        self.gui.equals()

        # Result should be 16 (8 * 2) if left-to-right evaluation
        result = float(self.gui.current_input)
        self.assertEqual(result, 16.0)

    def test_keyboard_input_mapping(self):
        """Test keyboard event handling."""
        # Create mock event objects
        mock_event = Mock()

        # Test number key
        mock_event.keysym = "5"
        with patch.object(self.gui, "number") as mock_number:
            self.gui.on_key_press(mock_event)
            mock_number.assert_called_with("5")

        # Test operation key
        mock_event.keysym = "+"
        with patch.object(self.gui, "operation") as mock_op:
            self.gui.on_key_press(mock_event)
            mock_op.assert_called_with("+")

        # Test enter key
        mock_event.keysym = "Return"
        with patch.object(self.gui, "equals") as mock_equals:
            self.gui.on_key_press(mock_event)
            mock_equals.assert_called()

    def test_history_integration(self):
        """Test integration with calculator history."""
        # Perform a calculation
        self.gui.current_input = "10"
        self.gui.operation("+")
        self.gui.current_input = "5"
        self.gui.equals()

        # Check that history was updated
        history = self.gui.calculator.get_history()
        self.assertTrue(len(history) > 0)
        self.assertIn("10", history[-1])
        self.assertIn("5", history[-1])
        self.assertIn("15", history[-1])

    def test_state_after_calculation(self):
        """Test GUI state management after calculations."""
        # Perform a calculation
        self.gui.current_input = "7"
        self.gui.operation("+")
        self.gui.current_input = "3"
        self.gui.equals()

        # After calculation, should be ready for new input
        self.assertTrue(self.gui.just_calculated)

        # New number should start fresh
        self.gui.number("5")
        self.assertEqual(self.gui.current_input, "5")
        self.assertFalse(self.gui.just_calculated)


class TestCalculatorGUIErrorHandling(unittest.TestCase):
    """Test error handling in the Calculator GUI."""

    def setUp(self):
        """Set up test fixtures."""
        self.mock_root = Mock(spec=tk.Tk)

        # Configure mock return values for screen methods
        self.mock_root.winfo_screenwidth.return_value = 1920
        self.mock_root.winfo_screenheight.return_value = 1080

        with patch("calculator_gui.tk.Tk"), patch(
            "calculator_gui.ttk.Frame"
        ), patch("calculator_gui.ttk.LabelFrame"), patch(
            "calculator_gui.ttk.Entry"
        ), patch(
            "calculator_gui.ttk.Button"
        ), patch(
            "calculator_gui.ttk.Style"
        ), patch(
            "calculator_gui.tk.StringVar"
        ) as mock_stringvar:
            # Mock StringVar
            mock_stringvar.return_value = Mock()

            self.gui = CalculatorGUI(self.mock_root)

    def test_division_by_zero(self):
        """Test division by zero error handling."""
        self.gui.current_input = "10"
        self.gui.operation("/")
        self.gui.current_input = "0"

        with patch.object(self.gui, "show_error") as mock_error:
            self.gui.equals()
            mock_error.assert_called_with("Cannot divide by zero")

    def test_invalid_factorial(self):
        """Test factorial with invalid input."""
        self.gui.current_input = "-5"

        with patch.object(self.gui, "show_error") as mock_error:
            self.gui.factorial()
            mock_error.assert_called()

    def test_invalid_square_root(self):
        """Test square root with negative number."""
        self.gui.current_input = "-4"

        with patch.object(self.gui, "show_error") as mock_error:
            self.gui.square_root()
            mock_error.assert_called()


class TestCalculatorGUIIntegration(unittest.TestCase):
    """Integration tests between GUI and Calculator class."""

    def setUp(self):
        """Set up test fixtures."""
        self.mock_root = Mock(spec=tk.Tk)

        # Configure mock return values for screen methods
        self.mock_root.winfo_screenwidth.return_value = 1920
        self.mock_root.winfo_screenheight.return_value = 1080

        with patch("calculator_gui.tk.Tk"), patch(
            "calculator_gui.ttk.Frame"
        ), patch("calculator_gui.ttk.LabelFrame"), patch(
            "calculator_gui.ttk.Entry"
        ), patch(
            "calculator_gui.ttk.Button"
        ), patch(
            "calculator_gui.ttk.Style"
        ), patch(
            "calculator_gui.tk.StringVar"
        ) as mock_stringvar:
            # Mock StringVar
            mock_stringvar.return_value = Mock()

            self.gui = CalculatorGUI(self.mock_root)

    def test_calculator_integration(self):
        """Test that GUI properly integrates with Calculator class."""
        # Verify calculator instance exists
        self.assertIsNotNone(self.gui.calculator)

        # Test that operations use the calculator
        self.gui.current_input = "8"
        self.gui.operation("+")
        self.gui.current_input = "2"
        self.gui.equals()

        # Verify result is stored in calculator
        last_result = self.gui.calculator.get_last_result()
        self.assertEqual(last_result, 10.0)

    def test_history_persistence(self):
        """Test that calculation history persists across operations."""
        # Perform multiple calculations
        calculations = [("5", "+", "3"), ("10", "-", "2"), ("4", "*", "3")]

        for a, op, b in calculations:
            self.gui.current_input = a
            self.gui.operation(op)
            self.gui.current_input = b
            self.gui.equals()

        # Check history
        history = self.gui.calculator.get_history()
        self.assertEqual(len(history), 3)


if __name__ == "__main__":
    # Run tests with minimal output for GUI testing
    unittest.main(verbosity=2)
