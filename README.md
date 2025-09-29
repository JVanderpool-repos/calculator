# 🧮 Python Calculator

A comprehensive Python calculator with both **command-line interface** and **graphical user interface**. Features basic arithmetic operations, advanced mathematical functions, trigonometry, and calculation history tracking.

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)
![GUI](https://img.shields.io/badge/GUI-tkinter-orange.svg)

## ✨ Features

### Basic Operations
- **Addition** (`+`): Add two numbers
- **Subtraction** (`-`): Subtract two numbers  
- **Multiplication** (`*`): Multiply two numbers
- **Division** (`/`): Divide two numbers with zero-division protection
- **Power** (`**`): Raise a number to a power

### Advanced Functions
- **Square Root** (`sqrt`): Calculate square roots
- **Percentage**: Calculate percentages (e.g., "20% of 150")
- **Factorial** (`!`): Calculate factorials
- **Logarithms**: Natural log (`ln`) and custom base (`log`)

### Trigonometric Functions
- **Sine** (`sin`): Calculate sine (degrees by default)
- **Cosine** (`cos`): Calculate cosine (degrees by default)
- **Tangent** (`tan`): Calculate tangent (degrees by default)

### Additional Features
- **Calculation History**: Track and display previous calculations
- **Error Handling**: Robust error handling with helpful messages
- **Interactive CLI**: User-friendly command-line interface
- **Graphical GUI**: Modern tkinter-based graphical interface
- **Batch Mode**: Execute single calculations from command line
- **Keyboard Support**: Full keyboard navigation in GUI mode
- **Modular API**: Use calculator functions in your own Python code

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/calculator.git
   cd calculator
   ```

2. **Choose your development environment:**

### Option A: DevContainer (Recommended)
   
   **Prerequisites:**
   - Docker Desktop installed and running
   - VS Code with the "Dev Containers" extension

   **Setup:**
   1. Open the project in VS Code
   2. When prompted, click "Reopen in Container" 
      - Or use Command Palette: `Dev Containers: Reopen in Container`
   3. Wait for the container to build (first time may take a few minutes)
   4. The development environment will be ready with all dependencies pre-installed!

   **Benefits:**
   - Consistent environment across all machines
   - No Python version conflicts
   - Pre-configured VS Code extensions
   - All development tools included

### Option B: Virtual Environment (Traditional)

   ```bash
   # Create virtual environment
   python -m venv .venv
   
   # Activate virtual environment
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Run the calculator:**
   ```bash
   python main.py
   ```

## 💻 Usage

The calculator supports three modes: **Interactive CLI**, **Batch Mode**, and **Graphical GUI**.

### 🖼️ Graphical User Interface (GUI)

Launch the modern graphical interface with:

```bash
python main.py --gui
```

The GUI features:
- **Visual calculator layout** with buttons for all operations
- **Keyboard support** for quick input (numbers, operators, Enter for equals)
- **History window** accessible via the "📜 History" button
- **Error dialogs** with helpful messages
- **Scientific functions** including trigonometry, factorial, square root
- **Memory operations** and calculation chaining
- **Responsive design** that works well in dev containers

**Keyboard Shortcuts in GUI:**
- `0-9`: Numbers
- `+`, `-`, `*`, `/`: Basic operations  
- `Enter` or `=`: Calculate result
- `Backspace`: Delete last digit
- `Escape`: Clear all
- `Delete`: Clear entry

### 🖥️ Interactive CLI Mode

Run the calculator without arguments to start interactive mode:

```bash
python main.py
```

This will start an interactive session where you can enter calculations:

```
==================================================
🧮 PYTHON CALCULATOR
==================================================
Available operations:
  Basic: +, -, *, /, ** (power)
  Advanced: sqrt, %, !, log, ln
  Trigonometric: sin, cos, tan (in degrees)
  Special commands:
    - history: Show calculation history
    - clear: Clear history
    - last: Show last result
    - help: Show this help
    - quit/exit: Exit calculator
==================================================
Enter calculations (e.g., '2 + 3', 'sqrt(16)', 'sin(90)'):

🧮 calc> 2 + 3
✅ 2.0 + 3.0 = 5.0

🧮 calc> sqrt(25)
✅ √25.0 = 5.0

🧮 calc> sin(90)
✅ sin(90.0°) = 1.0

🧮 calc> history
📜 History:
  1. 2 + 3 = 5.0
  2. √25.0 = 5.0
  3. sin(90.0°) = 1.0
```

### ⚡ Batch Mode

Execute single calculations directly from the command line:

```bash
python main.py "2 + 3"
# Output: ✅ 2.0 + 3.0 = 5.0

python main.py "sqrt(16)"
# Output: ✅ √16.0 = 4.0

python main.py "20% of 150"
# Output: ✅ 20.0% of 150.0 = 30.0
```

### 📖 Command Line Help

View all available options and examples:

```bash
python main.py --help
```

Output:
```
usage: main.py [-h] [--gui] [expression ...]

Python Calculator - CLI and GUI modes

positional arguments:
  expression  Mathematical expression to evaluate

options:
  -h, --help  show this help message and exit
  --gui       Launch calculator in GUI mode

Examples:
  calculator                    # Start interactive CLI
  calculator "2 + 3"             # Calculate expression directly
  calculator --gui              # Launch GUI mode
  calculator --gui "sin(90)"     # GUI mode with initial expression
```

### API Usage

Use the calculator in your Python code:

```python
from calculator import Calculator

# Create calculator instance
calc = Calculator()

# Basic operations
result = calc.add(10, 5)        # 15.0
result = calc.multiply(3, 4)    # 12.0
result = calc.divide(10, 2)     # 5.0

# Advanced operations
result = calc.square_root(25)   # 5.0
result = calc.factorial(5)      # 120
result = calc.percentage(100, 20)  # 20.0

# Trigonometry
result = calc.sine(90)          # 1.0 (degrees)
result = calc.cosine(0)         # 1.0 (degrees)

# Access history
history = calc.get_history()
last_result = calc.get_last_result()

# Convenience functions
from calculator import add, subtract, multiply, divide
result = add(5, 3)              # 8.0
```

## 📖 Expression Examples

| Expression | Description | Result |
|------------|-------------|--------|
| `2 + 3` | Basic addition | `5.0` |
| `10 - 4` | Basic subtraction | `6.0` |
| `5 * 6` | Basic multiplication | `30.0` |
| `15 / 3` | Basic division | `5.0` |
| `2 ** 3` | Power operation | `8.0` |
| `sqrt(25)` | Square root | `5.0` |
| `20% of 150` | Percentage calculation | `30.0` |
| `5!` | Factorial | `120` |
| `log(100, 10)` | Logarithm base 10 | `2.0` |
| `ln(2.718)` | Natural logarithm | `≈1.0` |
| `sin(90)` | Sine in degrees | `1.0` |
| `cos(0)` | Cosine in degrees | `1.0` |
| `tan(45)` | Tangent in degrees | `≈1.0` |

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
pytest

# Run tests with coverage report
pytest --cov=calculator tests/

# Run specific test file
pytest tests/test_calculator.py

# Run tests with verbose output
pytest -v
```

Test coverage includes:
- ✅ Unit tests for all calculator operations
- ✅ Integration tests for CLI functionality
- ✅ Error handling and edge cases
- ✅ Boundary condition testing
- ✅ History tracking functionality

## 🔧 Development

### Project Structure

```
calculator/
├── calculator.py           # Core calculator logic
├── main.py                # CLI application
├── __init__.py            # Package initialization
├── requirements.txt       # Project dependencies
├── README.md             # This file
├── .venv/                # Virtual environment
└── tests/                # Test suite
    ├── __init__.py
    ├── test_calculator.py # Calculator unit tests
    └── test_cli.py       # CLI integration tests
```

### Code Quality

The project includes tools for maintaining code quality:

```bash
# Format code with Black
black calculator.py main.py tests/

# Lint code with flake8
flake8 calculator.py main.py tests/

# Type checking with mypy
mypy calculator.py main.py
```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Ensure tests pass (`pytest`)
6. Format code (`black .`)
7. Commit changes (`git commit -m 'Add amazing feature'`)
8. Push to branch (`git push origin feature/amazing-feature`)
9. Open a Pull Request

## 📊 Error Handling

The calculator includes robust error handling:

- **Division by Zero**: Clear error message with prevention
- **Invalid Input**: Helpful guidance for correct syntax
- **Mathematical Errors**: Domain-specific error handling (e.g., sqrt of negative numbers)
- **Type Validation**: Ensures appropriate input types for operations

Example error scenarios:

```bash
🧮 calc> 5 / 0
❌ Error: Cannot divide by zero

🧮 calc> sqrt(-1)
❌ Error: Cannot calculate square root of negative number

🧮 calc> invalid expression
❌ Invalid expression. Type 'help' for usage examples.
```

## 🎯 Roadmap

Future enhancements planned:
- [ ] Graphical user interface (GUI)
- [ ] Scientific notation support
- [ ] Complex number operations
- [ ] Matrix calculations
- [ ] Unit conversions
- [ ] Expression evaluation with parentheses
- [ ] Variable storage and recall
- [ ] Function plotting capabilities

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/calculator/issues) page
2. Create a new issue with detailed information
3. Include error messages and steps to reproduce

## 🙏 Acknowledgments

- Built with Python 3.8+ for maximum compatibility
- Testing powered by pytest framework
- Code formatting by Black
- Inspired by the need for a simple, extensible calculator

---

**Happy Calculating!** 🧮✨