"""
Unit tests for the Calculator class.

This module contains comprehensive tests for all calculator operations
including basic arithmetic, advanced functions, and error handling.
"""

import pytest
import math
from calculator import Calculator, add, subtract, multiply, divide


class TestCalculator:
    """Test cases for the Calculator class."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()

    def test_addition(self):
        """Test addition operation."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0.5, 0.5) == 1.0
        assert self.calc.add(-5, -3) == -8

    def test_subtraction(self):
        """Test subtraction operation."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(-1, 1) == -2
        assert self.calc.subtract(0.5, 0.3) == pytest.approx(0.2)
        assert self.calc.subtract(-5, -3) == -2

    def test_multiplication(self):
        """Test multiplication operation."""
        assert self.calc.multiply(3, 4) == 12
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(0.5, 0.4) == pytest.approx(0.2)
        assert self.calc.multiply(0, 100) == 0

    def test_division(self):
        """Test division operation."""
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(-6, 2) == -3
        assert self.calc.divide(1, 3) == pytest.approx(0.3333333333333333)
        assert self.calc.divide(0, 5) == 0

    def test_division_by_zero(self):
        """Test division by zero raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            self.calc.divide(5, 0)

    def test_power(self):
        """Test power operation."""
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 2) == 25
        assert self.calc.power(2, 0) == 1
        assert self.calc.power(0, 5) == 0
        assert self.calc.power(-2, 3) == -8

    def test_square_root(self):
        """Test square root operation."""
        assert self.calc.square_root(25) == 5
        assert self.calc.square_root(16) == 4
        assert self.calc.square_root(0) == 0
        assert self.calc.square_root(2) == pytest.approx(1.4142135623730951)

    def test_square_root_negative(self):
        """Test square root of negative number raises ValueError."""
        with pytest.raises(ValueError):
            self.calc.square_root(-1)

    def test_percentage(self):
        """Test percentage calculation."""
        assert self.calc.percentage(100, 50) == 50
        assert self.calc.percentage(200, 25) == 50
        assert self.calc.percentage(0, 50) == 0
        assert self.calc.percentage(150, 20) == 30

    def test_factorial(self):
        """Test factorial calculation."""
        assert self.calc.factorial(0) == 1
        assert self.calc.factorial(1) == 1
        assert self.calc.factorial(5) == 120
        assert self.calc.factorial(6) == 720

    def test_factorial_negative(self):
        """Test factorial of negative number raises ValueError."""
        with pytest.raises(ValueError):
            self.calc.factorial(-1)

    def test_factorial_non_integer(self):
        """Test factorial of non-integer raises ValueError."""
        with pytest.raises(ValueError):
            self.calc.factorial(2.5)

    def test_logarithm_natural(self):
        """Test natural logarithm."""
        assert self.calc.logarithm(math.e) == pytest.approx(1.0)
        assert self.calc.logarithm(1) == pytest.approx(0.0)
        assert self.calc.logarithm(10) == pytest.approx(2.302585092994046)

    def test_logarithm_base_10(self):
        """Test logarithm base 10."""
        assert self.calc.logarithm(100, 10) == pytest.approx(2.0)
        assert self.calc.logarithm(1000, 10) == pytest.approx(3.0)
        assert self.calc.logarithm(1, 10) == pytest.approx(0.0)

    def test_logarithm_invalid_input(self):
        """Test logarithm with invalid input raises ValueError."""
        with pytest.raises(ValueError):
            self.calc.logarithm(0)  # Log of zero
        
        with pytest.raises(ValueError):
            self.calc.logarithm(-1)  # Log of negative number
        
        with pytest.raises(ValueError):
            self.calc.logarithm(10, 1)  # Base cannot be 1
        
        with pytest.raises(ValueError):
            self.calc.logarithm(10, -1)  # Base cannot be negative

    def test_sine(self):
        """Test sine function."""
        assert self.calc.sine(0) == pytest.approx(0.0)
        assert self.calc.sine(90) == pytest.approx(1.0)
        assert self.calc.sine(180) == pytest.approx(0.0)
        assert self.calc.sine(270) == pytest.approx(-1.0)

    def test_sine_radians(self):
        """Test sine function with radians."""
        assert self.calc.sine(0, degrees=False) == pytest.approx(0.0)
        assert self.calc.sine(math.pi/2, degrees=False) == pytest.approx(1.0)
        assert self.calc.sine(math.pi, degrees=False) == pytest.approx(0.0)

    def test_cosine(self):
        """Test cosine function."""
        assert self.calc.cosine(0) == pytest.approx(1.0)
        assert self.calc.cosine(90) == pytest.approx(0.0)
        assert self.calc.cosine(180) == pytest.approx(-1.0)
        assert self.calc.cosine(270) == pytest.approx(0.0)

    def test_cosine_radians(self):
        """Test cosine function with radians."""
        assert self.calc.cosine(0, degrees=False) == pytest.approx(1.0)
        assert self.calc.cosine(math.pi/2, degrees=False) == pytest.approx(0.0)
        assert self.calc.cosine(math.pi, degrees=False) == pytest.approx(-1.0)

    def test_tangent(self):
        """Test tangent function."""
        assert self.calc.tangent(0) == pytest.approx(0.0)
        assert self.calc.tangent(45) == pytest.approx(1.0)
        assert self.calc.tangent(180) == pytest.approx(0.0)

    def test_tangent_radians(self):
        """Test tangent function with radians."""
        assert self.calc.tangent(0, degrees=False) == pytest.approx(0.0)
        assert self.calc.tangent(math.pi/4, degrees=False) == pytest.approx(1.0)
        assert self.calc.tangent(math.pi, degrees=False) == pytest.approx(0.0)

    def test_history_tracking(self):
        """Test that operations are tracked in history."""
        self.calc.add(2, 3)
        self.calc.multiply(4, 5)
        
        history = self.calc.get_history()
        assert len(history) == 2
        assert "2 + 3 = 5" in history[0]
        assert "4 × 5 = 20" in history[1]

    def test_last_result_tracking(self):
        """Test that last result is tracked correctly."""
        result = self.calc.add(10, 5)
        assert self.calc.get_last_result() == result == 15
        
        result = self.calc.multiply(3, 7)
        assert self.calc.get_last_result() == result == 21

    def test_clear_history(self):
        """Test clearing calculation history."""
        self.calc.add(1, 1)
        self.calc.subtract(5, 3)
        
        assert len(self.calc.get_history()) == 2
        
        self.calc.clear_history()
        assert len(self.calc.get_history()) == 0

    def test_history_independence(self):
        """Test that get_history returns a copy, not the original list."""
        self.calc.add(1, 1)
        history = self.calc.get_history()
        history.append("fake entry")
        
        # Original history should be unchanged
        assert len(self.calc.get_history()) == 1
        assert "fake entry" not in self.calc.get_history()


class TestConvenienceFunctions:
    """Test cases for convenience functions."""

    def test_add_function(self):
        """Test standalone add function."""
        assert add(2, 3) == 5

    def test_subtract_function(self):
        """Test standalone subtract function."""
        assert subtract(5, 3) == 2

    def test_multiply_function(self):
        """Test standalone multiply function."""
        assert multiply(4, 5) == 20

    def test_divide_function(self):
        """Test standalone divide function."""
        assert divide(10, 2) == 5

    def test_divide_function_zero_error(self):
        """Test standalone divide function with zero divisor."""
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)


class TestEdgeCases:
    """Test cases for edge cases and boundary conditions."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()

    def test_very_large_numbers(self):
        """Test operations with very large numbers."""
        large_num = 10**100
        assert self.calc.add(large_num, 1) == large_num + 1

    def test_very_small_numbers(self):
        """Test operations with very small numbers."""
        small_num = 10**(-100)
        result = self.calc.add(small_num, small_num)
        assert result == 2 * small_num

    def test_floating_point_precision(self):
        """Test floating point precision issues."""
        # This test shows the limitation of floating point arithmetic
        result = self.calc.add(0.1, 0.2)
        assert result == pytest.approx(0.3)

    def test_zero_operations(self):
        """Test various operations with zero."""
        assert self.calc.add(0, 0) == 0
        assert self.calc.subtract(0, 0) == 0
        assert self.calc.multiply(0, 100) == 0
        assert self.calc.multiply(100, 0) == 0
        assert self.calc.divide(0, 5) == 0
        assert self.calc.power(0, 5) == 0
        assert self.calc.power(5, 0) == 1