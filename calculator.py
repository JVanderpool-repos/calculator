"""
Calculator Module

A comprehensive calculator implementation with basic and advanced operations.
Includes error handling and support for various mathematical operations.
"""

import math
from typing import Union, List


class Calculator:
    """
    A calculator class that provides basic and advanced mathematical operations.
    """

    def __init__(self):
        """Initialize the calculator."""
        self.history: List[str] = []
        self.last_result: Union[int, float] = 0

    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b
        """
        result = a + b
        self.last_result = result
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Subtract b from a.

        Args:
            a: First number
            b: Second number

        Returns:
            Difference of a and b
        """
        result = a - b
        self.last_result = result
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Product of a and b
        """
        result = a * b
        self.last_result = result
        self.history.append(f"{a} × {b} = {result}")
        return result

    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Divide a by b.

        Args:
            a: Dividend
            b: Divisor

        Returns:
            Quotient of a and b

        Raises:
            ZeroDivisionError: If b is zero
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        result = a / b
        self.last_result = result
        self.history.append(f"{a} ÷ {b} = {result}")
        return result

    def power(
        self, base: Union[int, float], exponent: Union[int, float]
    ) -> Union[int, float]:
        """
        Raise base to the power of exponent.

        Args:
            base: The base number
            exponent: The exponent

        Returns:
            base raised to the power of exponent
        """
        result = base**exponent
        self.last_result = result
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result

    def square_root(self, number: Union[int, float]) -> float:
        """
        Calculate the square root of a number.

        Args:
            number: The number to find square root of

        Returns:
            Square root of the number

        Raises:
            ValueError: If number is negative
        """
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")

        result = math.sqrt(number)
        self.last_result = result
        self.history.append(f"√{number} = {result}")
        return result

    def percentage(
        self, number: Union[int, float], percent: Union[int, float]
    ) -> Union[int, float]:
        """
        Calculate percentage of a number.

        Args:
            number: The base number
            percent: The percentage to calculate

        Returns:
            percent% of number
        """
        result = (number * percent) / 100
        self.last_result = result
        self.history.append(f"{percent}% of {number} = {result}")
        return result

    def factorial(self, n: int) -> int:
        """
        Calculate factorial of a number.

        Args:
            n: The number to calculate factorial of

        Returns:
            Factorial of n

        Raises:
            ValueError: If n is negative or not an integer
        """
        if not isinstance(n, int) or n < 0:
            raise ValueError("Factorial is only defined for non-negative integers")

        result = math.factorial(n)
        self.last_result = result
        self.history.append(f"{n}! = {result}")
        return result

    def logarithm(
        self, number: Union[int, float], base: Union[int, float] = math.e
    ) -> float:
        """
        Calculate logarithm of a number with given base.

        Args:
            number: The number to calculate logarithm of
            base: The logarithm base (default is e for natural log)

        Returns:
            Logarithm of number with given base

        Raises:
            ValueError: If number <= 0 or base <= 0 or base == 1
        """
        if number <= 0:
            raise ValueError("Logarithm is only defined for positive numbers")
        if base <= 0 or base == 1:
            raise ValueError("Logarithm base must be positive and not equal to 1")

        if base == math.e:
            result = math.log(number)
            self.history.append(f"ln({number}) = {result}")
        else:
            result = math.log(number, base)
            self.history.append(f"log_{base}({number}) = {result}")

        self.last_result = result
        return result

    def sine(self, angle: Union[int, float], degrees: bool = True) -> float:
        """
        Calculate sine of an angle.

        Args:
            angle: The angle
            degrees: Whether the angle is in degrees (True) or radians (False)

        Returns:
            Sine of the angle
        """
        if degrees:
            angle_rad = math.radians(angle)
            self.history.append(f"sin({angle}°) = {math.sin(angle_rad)}")
        else:
            angle_rad = angle
            self.history.append(f"sin({angle} rad) = {math.sin(angle_rad)}")

        result = math.sin(angle_rad)
        self.last_result = result
        return result

    def cosine(self, angle: Union[int, float], degrees: bool = True) -> float:
        """
        Calculate cosine of an angle.

        Args:
            angle: The angle
            degrees: Whether the angle is in degrees (True) or radians (False)

        Returns:
            Cosine of the angle
        """
        if degrees:
            angle_rad = math.radians(angle)
            self.history.append(f"cos({angle}°) = {math.cos(angle_rad)}")
        else:
            angle_rad = angle
            self.history.append(f"cos({angle} rad) = {math.cos(angle_rad)}")

        result = math.cos(angle_rad)
        self.last_result = result
        return result

    def tangent(self, angle: Union[int, float], degrees: bool = True) -> float:
        """
        Calculate tangent of an angle.

        Args:
            angle: The angle
            degrees: Whether the angle is in degrees (True) or radians (False)

        Returns:
            Tangent of the angle
        """
        if degrees:
            angle_rad = math.radians(angle)
            self.history.append(f"tan({angle}°) = {math.tan(angle_rad)}")
        else:
            angle_rad = angle
            self.history.append(f"tan({angle} rad) = {math.tan(angle_rad)}")

        result = math.tan(angle_rad)
        self.last_result = result
        return result

    def clear_history(self) -> None:
        """Clear the calculation history."""
        self.history.clear()

    def get_history(self) -> List[str]:
        """
        Get the calculation history.

        Returns:
            List of calculation strings
        """
        return self.history.copy()

    def get_last_result(self) -> Union[int, float]:
        """
        Get the last calculation result.

        Returns:
            The last calculation result
        """
        return self.last_result


# Convenience functions for direct use
def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers."""
    calc = Calculator()
    return calc.add(a, b)


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Subtract b from a."""
    calc = Calculator()
    return calc.subtract(a, b)


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Multiply two numbers."""
    calc = Calculator()
    return calc.multiply(a, b)


def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Divide a by b."""
    calc = Calculator()
    return calc.divide(a, b)
