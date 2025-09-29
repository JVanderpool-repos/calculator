"""
Integration tests for the Calculator CLI.

This module contains tests for the command-line interface functionality
including expression parsing and user interaction scenarios.
"""

import sys
from io import StringIO
from unittest.mock import patch

import pytest

from main import CalculatorCLI


class TestCalculatorCLI:
    """Test cases for the Calculator CLI."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.cli = CalculatorCLI()

    def test_basic_arithmetic_parsing(self):
        """Test parsing of basic arithmetic expressions."""
        assert "✅ 2.0 + 3.0 = 5.0" in self.cli.parse_expression("2 + 3")
        assert "✅ 10.0 - 4.0 = 6.0" in self.cli.parse_expression("10 - 4")
        assert "✅ 5.0 * 6.0 = 30.0" in self.cli.parse_expression("5 * 6")
        assert "✅ 15.0 / 3.0 = 5.0" in self.cli.parse_expression("15 / 3")

    def test_power_expression_parsing(self):
        """Test parsing of power expressions."""
        result = self.cli.parse_expression("2 ** 3")
        assert "✅ 2.0^3.0 = 8.0" in result

    def test_square_root_parsing(self):
        """Test parsing of square root expressions."""
        result = self.cli.parse_expression("sqrt(25)")
        assert "✅ √25.0 = 5.0" in result

    def test_percentage_parsing(self):
        """Test parsing of percentage expressions."""
        result = self.cli.parse_expression("20% of 150")
        assert "✅ 20.0% of 150.0 = 30.0" in result

    def test_factorial_parsing(self):
        """Test parsing of factorial expressions."""
        result = self.cli.parse_expression("5!")
        assert "✅ 5! = 120" in result

    def test_logarithm_parsing(self):
        """Test parsing of logarithm expressions."""
        result = self.cli.parse_expression("log(100, 10)")
        assert "✅ log₍10.0₎(100.0) = 2.0" in result

        result = self.cli.parse_expression("ln(2.718)")
        assert "ln(2.718)" in result

    def test_trigonometric_parsing(self):
        """Test parsing of trigonometric expressions."""
        result = self.cli.parse_expression("sin(90)")
        assert "sin(90.0°)" in result and "1.0" in result

        result = self.cli.parse_expression("cos(0)")
        assert "cos(0.0°)" in result and "1.0" in result

        result = self.cli.parse_expression("tan(45)")
        assert "tan(45.0°)" in result

    def test_special_commands(self):
        """Test special command parsing."""
        # Test quit command
        result = self.cli.parse_expression("quit")
        assert "👋 Goodbye!" in result
        assert not self.cli.running

        # Reset for other tests
        self.cli.running = True

        # Test exit command
        result = self.cli.parse_expression("exit")
        assert "👋 Goodbye!" in result
        assert not self.cli.running

        # Reset for other tests
        self.cli.running = True

        # Test clear command
        self.cli.calculator.add(1, 1)  # Add something to history
        result = self.cli.parse_expression("clear")
        assert "🗑️  History cleared" in result
        assert len(self.cli.calculator.get_history()) == 0

        # Test last command
        self.cli.calculator.add(5, 5)
        result = self.cli.parse_expression("last")
        assert "🔢 Last result: 10" in result

    def test_history_command(self):
        """Test history command."""
        # Empty history
        result = self.cli.parse_expression("history")
        assert "📜 No calculations in history" in result

        # Add some calculations
        self.cli.calculator.add(1, 2)
        self.cli.calculator.multiply(3, 4)

        result = self.cli.parse_expression("history")
        assert "📜 History:" in result
        assert "1 + 2 = 3" in result
        assert "3 × 4 = 12" in result

    def test_error_handling(self):
        """Test error handling in expression parsing."""
        # Division by zero
        result = self.cli.parse_expression("5 / 0")
        assert "❌ Error: Cannot divide by zero" in result

        # Invalid expression
        result = self.cli.parse_expression("invalid expression")
        assert "❌ Invalid expression" in result

        # Square root of negative number
        result = self.cli.parse_expression("sqrt(-1)")
        assert "❌ Invalid expression" in result

    def test_case_insensitive_input(self):
        """Test that input is case insensitive."""
        result1 = self.cli.parse_expression("SQRT(25)")
        result2 = self.cli.parse_expression("sqrt(25)")
        # Both should work and produce similar results
        assert "√25.0 = 5.0" in result1
        assert "√25.0 = 5.0" in result2

    def test_whitespace_handling(self):
        """Test that extra whitespace is handled correctly."""
        result = self.cli.parse_expression("  2   +   3  ")
        assert "✅ 2.0 + 3.0 = 5.0" in result

    @patch("builtins.input", side_effect=["2 + 3", "quit"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_interactive_mode_basic(self, mock_stdout, mock_input):
        """Test basic interactive mode functionality."""
        # Override the display_welcome method to avoid printing during tests
        with patch.object(self.cli, "display_welcome"):
            self.cli.run_interactive()

        output = mock_stdout.getvalue()
        assert "✅ 2.0 + 3.0 = 5.0" in output or "2.0 + 3.0 = 5.0" in str(mock_stdout)

    def test_single_command_mode(self):
        """Test single command mode."""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.cli.run_single_command("2 + 3")
            output = mock_stdout.getvalue()
            assert "✅ 2.0 + 3.0 = 5.0" in output


class TestCLIEdgeCases:
    """Test edge cases for the CLI."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.cli = CalculatorCLI()

    def test_empty_input(self):
        """Test handling of empty input."""
        # Empty string should not cause errors in interactive mode
        result = self.cli.parse_expression("")
        # Should return invalid expression message for empty input
        assert "❌ Invalid expression" in result

    def test_multiple_operators(self):
        """Test expressions with multiple operators (supported by eval fallback)."""
        # This should work with eval fallback
        result = self.cli.parse_expression("2 + 3 * 4")
        assert "✅" in result and "14" in result

    def test_complex_expressions(self):
        """Test complex mathematical expressions."""
        # Test expressions that might work with eval fallback
        result = self.cli.parse_expression("2 * 3")
        assert "✅ 2.0 * 3.0 = 6.0" in result

    def test_help_command_output(self):
        """Test that help command produces output."""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            result = self.cli.parse_expression("help")
            self.cli.display_help()

            # The result should be empty (help prints directly)
            assert result == ""

            # But stdout should contain help information
            output = mock_stdout.getvalue()
            assert "CALCULATOR HELP" in output
            assert "Basic Operations:" in output
