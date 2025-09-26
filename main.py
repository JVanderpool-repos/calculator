#!/usr/bin/env python3
"""
Calculator CLI Application

A command-line interface for the Python calculator with interactive mode
and direct calculation support.
"""

import sys
import re
from calculator import Calculator


class CalculatorCLI:
    """Command-line interface for the calculator."""
    
    def __init__(self):
        """Initialize the CLI calculator."""
        self.calculator = Calculator()
        self.running = True

    def display_welcome(self):
        """Display welcome message and available commands."""
        print("=" * 50)
        print("🧮 PYTHON CALCULATOR")
        print("=" * 50)
        print("Available operations:")
        print("  Basic: +, -, *, /, ** (power)")
        print("  Advanced: sqrt, %, !, log, ln")
        print("  Trigonometric: sin, cos, tan (in degrees)")
        print("  Special commands:")
        print("    - history: Show calculation history")
        print("    - clear: Clear history")
        print("    - last: Show last result")
        print("    - help: Show this help")
        print("    - quit/exit: Exit calculator")
        print("=" * 50)
        print("Enter calculations (e.g., '2 + 3', 'sqrt(16)', 'sin(90)'):")
        print()

    def display_help(self):
        """Display detailed help information."""
        print("\n📖 CALCULATOR HELP")
        print("-" * 30)
        print("Basic Operations:")
        print("  2 + 3        → Addition")
        print("  10 - 4       → Subtraction")
        print("  5 * 6        → Multiplication")
        print("  15 / 3       → Division")
        print("  2 ** 3       → Power (2^3)")
        print()
        print("Advanced Operations:")
        print("  sqrt(25)     → Square root")
        print("  20% of 150   → Percentage")
        print("  5!           → Factorial")
        print("  log(100, 10) → Logarithm base 10")
        print("  ln(2.718)    → Natural logarithm")
        print()
        print("Trigonometric (degrees):")
        print("  sin(90)      → Sine")
        print("  cos(0)       → Cosine")
        print("  tan(45)      → Tangent")
        print()
        print("Special Commands:")
        print("  history      → Show calculation history")
        print("  clear        → Clear history")
        print("  last         → Show last result")
        print("  quit/exit    → Exit calculator")
        print("-" * 30)

    def parse_expression(self, expression: str) -> str:
        """
        Parse and evaluate mathematical expressions.
        
        Args:
            expression: The mathematical expression to evaluate
            
        Returns:
            String representation of the result
        """
        expression = expression.strip().lower()
        
        try:
            # Handle special commands
            if expression in ['quit', 'exit']:
                self.running = False
                return "👋 Goodbye!"
            
            elif expression == 'help':
                self.display_help()
                return ""
            
            elif expression == 'history':
                history = self.calculator.get_history()
                if not history:
                    return "📜 No calculations in history"
                return "📜 History:\n" + "\n".join(f"  {i+1}. {calc}" for i, calc in enumerate(history[-10:]))
            
            elif expression == 'clear':
                self.calculator.clear_history()
                return "🗑️  History cleared"
            
            elif expression == 'last':
                return f"🔢 Last result: {self.calculator.get_last_result()}"
            
            # Handle percentage expressions (e.g., "20% of 150")
            percentage_match = re.match(r'(\d+(?:\.\d+)?)%\s+of\s+(\d+(?:\.\d+)?)', expression)
            if percentage_match:
                percent, number = float(percentage_match.group(1)), float(percentage_match.group(2))
                result = self.calculator.percentage(number, percent)
                return f"✅ {percent}% of {number} = {result}"
            
            # Handle factorial expressions (e.g., "5!")
            factorial_match = re.match(r'(\d+)!', expression)
            if factorial_match:
                number = int(factorial_match.group(1))
                result = self.calculator.factorial(number)
                return f"✅ {number}! = {result}"
            
            # Handle square root expressions (e.g., "sqrt(25)")
            sqrt_match = re.match(r'sqrt\((\d+(?:\.\d+)?)\)', expression)
            if sqrt_match:
                number = float(sqrt_match.group(1))
                result = self.calculator.square_root(number)
                return f"✅ √{number} = {result}"
            
            # Handle logarithm expressions (e.g., "log(100, 10)" or "ln(2.718)")
            log_match = re.match(r'log\((\d+(?:\.\d+)?),\s*(\d+(?:\.\d+)?)\)', expression)
            if log_match:
                number, base = float(log_match.group(1)), float(log_match.group(2))
                result = self.calculator.logarithm(number, base)
                return f"✅ log₍{base}₎({number}) = {result}"
            
            ln_match = re.match(r'ln\((\d+(?:\.\d+)?)\)', expression)
            if ln_match:
                number = float(ln_match.group(1))
                result = self.calculator.logarithm(number)
                return f"✅ ln({number}) = {result}"
            
            # Handle trigonometric functions
            trig_match = re.match(r'(sin|cos|tan)\((\d+(?:\.\d+)?)\)', expression)
            if trig_match:
                func_name, angle = trig_match.group(1), float(trig_match.group(2))
                if func_name == 'sin':
                    result = self.calculator.sine(angle)
                elif func_name == 'cos':
                    result = self.calculator.cosine(angle)
                else:  # tan
                    result = self.calculator.tangent(angle)
                return f"✅ {func_name}({angle}°) = {result}"
            
            # Handle basic arithmetic expressions
            # Replace ** with power function for better tracking
            if '**' in expression:
                power_match = re.match(r'(\d+(?:\.\d+)?)\s*\*\*\s*(\d+(?:\.\d+)?)', expression)
                if power_match:
                    base, exponent = float(power_match.group(1)), float(power_match.group(2))
                    result = self.calculator.power(base, exponent)
                    return f"✅ {base}^{exponent} = {result}"
            
            # Handle basic operations
            operators = {
                '+': self.calculator.add,
                '-': self.calculator.subtract,
                '*': self.calculator.multiply,
                '/': self.calculator.divide
            }
            
            for op_symbol, op_func in operators.items():
                if op_symbol in expression:
                    parts = expression.split(op_symbol)
                    if len(parts) == 2:
                        try:
                            a, b = float(parts[0].strip()), float(parts[1].strip())
                            result = op_func(a, b)
                            return f"✅ {a} {op_symbol} {b} = {result}"
                        except ValueError:
                            continue
            
            # If no pattern matched, try to evaluate as Python expression (with caution)
            # This is a fallback for complex expressions
            try:
                result = eval(expression, {"__builtins__": {}}, {})
                if isinstance(result, (int, float)):
                    return f"✅ {expression} = {result}"
            except:
                pass
            
            return "❌ Invalid expression. Type 'help' for usage examples."
        
        except ZeroDivisionError:
            return "❌ Error: Cannot divide by zero"
        except ValueError as e:
            return f"❌ Error: {str(e)}"
        except Exception as e:
            return f"❌ Error: {str(e)}"

    def run_interactive(self):
        """Run the calculator in interactive mode."""
        self.display_welcome()
        
        while self.running:
            try:
                user_input = input("🧮 calc> ").strip()
                
                if not user_input:
                    continue
                
                result = self.parse_expression(user_input)
                if result:
                    print(result)
                    
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except EOFError:
                print("\n👋 Goodbye!")
                break

    def run_single_command(self, expression: str):
        """
        Run a single calculation and exit.
        
        Args:
            expression: The mathematical expression to evaluate
        """
        result = self.parse_expression(expression)
        if result:
            print(result)


def main():
    """Main entry point for the calculator CLI."""
    cli = CalculatorCLI()
    
    if len(sys.argv) > 1:
        # Run single command mode
        expression = " ".join(sys.argv[1:])
        cli.run_single_command(expression)
    else:
        # Run interactive mode
        cli.run_interactive()


if __name__ == "__main__":
    main()