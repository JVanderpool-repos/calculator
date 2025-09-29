#!/usr/bin/env python3
"""
Calculator GUI Application

A tkinter-based graphical user interface for the Python calculator.
Provides an intuitive calculator interface with buttons and keyboard support.
"""

import tkinter as tk
from tkinter import messagebox, ttk

from calculator import Calculator


class CalculatorGUI:
    """
    A tkinter-based GUI for the calculator application.

    Provides a user-friendly interface with:
    - Numeric keypad (0-9)
    - Basic operations (+, -, *, /)
    - Advanced operations (√, %, ^, !)
    - Trigonometric functions (sin, cos, tan)
    - Memory functions (clear, history)
    - Keyboard support
    """

    def __init__(self, root):
        """Initialize the calculator GUI."""
        self.root = root
        self.calculator = Calculator()
        self.setup_window()
        self.create_variables()
        self.create_widgets()
        self.bind_keyboard_events()

    def setup_window(self):
        """Configure the main window properties."""
        self.root.title("🧮 Python Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        # Center the window on screen
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.root.winfo_screenheight() // 2) - (600 // 2)
        self.root.geometry(f"400x600+{x}+{y}")

    def create_variables(self):
        """Create tkinter variables for the display and state management."""
        self.display_var = tk.StringVar(value="0")
        self.current_input = ""
        self.pending_operation = None
        self.pending_value = None
        self.last_operation = None
        self.just_calculated = False

    def create_widgets(self):
        """Create and arrange all GUI widgets."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Display frame
        display_frame = ttk.LabelFrame(main_frame, text="Display", padding="5")
        display_frame.grid(
            row=0, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=(0, 10)
        )

        # Display entry
        self.display = ttk.Entry(
            display_frame,
            textvariable=self.display_var,
            font=("Arial", 16, "bold"),
            justify="right",
            state="readonly",
            width=25,
        )
        self.display.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=5, pady=5)

        # History button
        history_btn = ttk.Button(
            display_frame,
            text="📜 History",
            command=self.show_history,
            width=10,
        )
        history_btn.grid(row=1, column=0, sticky=tk.W, padx=5, pady=(0, 5))

        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=1, column=0, columnspan=4)

        # Create button layout
        self.create_buttons(button_frame)

        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        display_frame.columnconfigure(0, weight=1)

    def create_buttons(self, parent):
        """Create calculator buttons with proper styling."""
        # Button style configuration
        style = ttk.Style()
        style.configure("Num.TButton", font=("Arial", 12, "bold"))
        style.configure("Op.TButton", font=("Arial", 12, "bold"))
        style.configure("Special.TButton", font=("Arial", 10, "bold"))

        # Button layout definition
        buttons = [
            # Row 1: Memory and advanced functions
            [
                ("C", self.clear, "Special.TButton"),
                ("CE", self.clear_entry, "Special.TButton"),
                ("⌫", self.backspace, "Special.TButton"),
                ("/", lambda: self.operation("/"), "Op.TButton"),
            ],
            # Row 2: Numbers and operations
            [
                ("7", lambda: self.number("7"), "Num.TButton"),
                ("8", lambda: self.number("8"), "Num.TButton"),
                ("9", lambda: self.number("9"), "Num.TButton"),
                ("*", lambda: self.operation("*"), "Op.TButton"),
            ],
            # Row 3: Numbers and operations
            [
                ("4", lambda: self.number("4"), "Num.TButton"),
                ("5", lambda: self.number("5"), "Num.TButton"),
                ("6", lambda: self.number("6"), "Num.TButton"),
                ("-", lambda: self.operation("-"), "Op.TButton"),
            ],
            # Row 4: Numbers and operations
            [
                ("1", lambda: self.number("1"), "Num.TButton"),
                ("2", lambda: self.number("2"), "Num.TButton"),
                ("3", lambda: self.number("3"), "Num.TButton"),
                ("+", lambda: self.operation("+"), "Op.TButton"),
            ],
            # Row 5: Zero, decimal, equals
            [
                ("0", lambda: self.number("0"), "Num.TButton"),
                (".", self.decimal, "Num.TButton"),
                ("=", self.equals, "Op.TButton"),
                ("±", self.toggle_sign, "Op.TButton"),
            ],
            # Row 6: Advanced functions
            [
                ("√", self.square_root, "Special.TButton"),
                ("x²", self.square, "Special.TButton"),
                ("xʸ", lambda: self.operation("**"), "Special.TButton"),
                ("%", self.percentage, "Special.TButton"),
            ],
            # Row 7: Trigonometric functions
            [
                ("sin", self.sine, "Special.TButton"),
                ("cos", self.cosine, "Special.TButton"),
                ("tan", self.tangent, "Special.TButton"),
                ("!", self.factorial, "Special.TButton"),
            ],
        ]

        # Create buttons
        for row_idx, row in enumerate(buttons):
            for col_idx, (text, command, style_name) in enumerate(row):
                btn = ttk.Button(
                    parent,
                    text=text,
                    command=command,
                    style=style_name,
                    width=8,
                )
                btn.grid(
                    row=row_idx,
                    column=col_idx,
                    padx=2,
                    pady=2,
                    sticky=(tk.W, tk.E),
                )

        # Configure grid weights for responsive design
        for i in range(4):
            parent.columnconfigure(i, weight=1)

    def bind_keyboard_events(self):
        """Bind keyboard events for calculator input."""
        self.root.bind("<Key>", self.on_key_press)
        self.root.focus_set()  # Ensure window can receive keyboard events

    def on_key_press(self, event):
        """Handle keyboard input."""
        key = event.keysym

        # Numbers
        if key.isdigit():
            self.number(key)
        # Operations
        elif key in ["+", "-", "*", "/"]:
            self.operation(key)
        elif key == "Return" or key == "equal":
            self.equals()
        elif key == "period":
            self.decimal()
        elif key == "BackSpace":
            self.backspace()
        elif key == "Escape":
            self.clear()
        elif key == "Delete":
            self.clear_entry()

    def number(self, digit):
        """Handle number button press."""
        if self.just_calculated:
            self.current_input = ""
            self.just_calculated = False

        if self.current_input == "0":
            self.current_input = digit
        else:
            self.current_input += digit

        self.update_display(self.current_input)

    def decimal(self):
        """Handle decimal point button press."""
        if self.just_calculated:
            self.current_input = "0"
            self.just_calculated = False

        if "." not in self.current_input:
            if not self.current_input:
                self.current_input = "0"
            self.current_input += "."
            self.update_display(self.current_input)

    def operation(self, op):
        """Handle operation button press."""
        try:
            if self.current_input:
                current_value = float(self.current_input)

                if self.pending_operation and not self.just_calculated:
                    # Chain operations
                    self.equals()
                    current_value = self.calculator.get_last_result()

                self.pending_value = current_value
                self.pending_operation = op
                self.current_input = ""
                self.just_calculated = False

        except ValueError:
            self.show_error("Invalid number")

    def equals(self):
        """Handle equals button press."""
        try:
            if self.pending_operation and self.pending_value is not None:
                if self.current_input:
                    current_value = float(self.current_input)
                else:
                    current_value = self.pending_value

                # Perform calculation using Calculator class
                if self.pending_operation == "+":
                    result = self.calculator.add(
                        self.pending_value, current_value
                    )
                elif self.pending_operation == "-":
                    result = self.calculator.subtract(
                        self.pending_value, current_value
                    )
                elif self.pending_operation == "*":
                    result = self.calculator.multiply(
                        self.pending_value, current_value
                    )
                elif self.pending_operation == "/":
                    if current_value == 0:
                        raise ZeroDivisionError("Cannot divide by zero")
                    result = self.calculator.divide(
                        self.pending_value, current_value
                    )
                elif self.pending_operation == "**":
                    result = self.calculator.power(
                        self.pending_value, current_value
                    )
                else:
                    return

                self.update_display(str(result))
                self.current_input = str(result)
                self.pending_operation = None
                self.pending_value = None
                self.just_calculated = True

        except ZeroDivisionError as e:
            self.show_error(str(e))
        except Exception as e:
            self.show_error(f"Error: {str(e)}")

    def clear(self):
        """Clear all calculator state."""
        self.current_input = ""
        self.pending_operation = None
        self.pending_value = None
        self.just_calculated = False
        self.update_display("0")

    def clear_entry(self):
        """Clear current entry only."""
        self.current_input = ""
        self.update_display("0")

    def backspace(self):
        """Remove last character from current input."""
        if self.current_input and not self.just_calculated:
            self.current_input = self.current_input[:-1]
            if not self.current_input:
                self.update_display("0")
            else:
                self.update_display(self.current_input)

    def toggle_sign(self):
        """Toggle the sign of current number."""
        if self.current_input and self.current_input != "0":
            if self.current_input.startswith("-"):
                self.current_input = self.current_input[1:]
            else:
                self.current_input = "-" + self.current_input
            self.update_display(self.current_input)

    def square_root(self):
        """Calculate square root of current number."""
        try:
            if self.current_input:
                value = float(self.current_input)
            else:
                value = 0

            result = self.calculator.square_root(value)
            self.update_display(str(result))
            self.current_input = str(result)
            self.just_calculated = True

        except ValueError as e:
            self.show_error(str(e))
        except Exception as e:
            self.show_error(f"Error: {str(e)}")

    def square(self):
        """Calculate square of current number."""
        try:
            if self.current_input:
                value = float(self.current_input)
                result = self.calculator.power(value, 2)
                self.update_display(str(result))
                self.current_input = str(result)
                self.just_calculated = True
        except Exception as e:
            self.show_error(f"Error: {str(e)}")

    def percentage(self):
        """Calculate percentage (divide by 100)."""
        try:
            if self.current_input:
                value = float(self.current_input)
                result = value / 100
                self.update_display(str(result))
                self.current_input = str(result)
                self.just_calculated = True
        except Exception as e:
            self.show_error(f"Error: {str(e)}")

    def factorial(self):
        """Calculate factorial of current number."""
        try:
            if self.current_input:
                value = int(float(self.current_input))
                result = self.calculator.factorial(value)
                self.update_display(str(result))
                self.current_input = str(result)
                self.just_calculated = True
        except Exception as e:
            self.show_error(f"Error: {str(e)}")

    def sine(self):
        """Calculate sine of current number (in degrees)."""
        try:
            if self.current_input:
                value = float(self.current_input)
                result = self.calculator.sine(value, degrees=True)
                self.update_display(str(result))
                self.current_input = str(result)
                self.just_calculated = True
        except Exception as e:
            self.show_error(f"Error: {str(e)}")

    def cosine(self):
        """Calculate cosine of current number (in degrees)."""
        try:
            if self.current_input:
                value = float(self.current_input)
                result = self.calculator.cosine(value, degrees=True)
                self.update_display(str(result))
                self.current_input = str(result)
                self.just_calculated = True
        except Exception as e:
            self.show_error(f"Error: {str(e)}")

    def tangent(self):
        """Calculate tangent of current number (in degrees)."""
        try:
            if self.current_input:
                value = float(self.current_input)
                result = self.calculator.tangent(value, degrees=True)
                self.update_display(str(result))
                self.current_input = str(result)
                self.just_calculated = True
        except Exception as e:
            self.show_error(f"Error: {str(e)}")

    def show_history(self):
        """Display calculation history in a popup window."""
        history = self.calculator.get_history()

        if not history:
            messagebox.showinfo("History", "No calculations in history.")
            return

        # Create history window
        history_window = tk.Toplevel(self.root)
        history_window.title("📜 Calculation History")
        history_window.geometry("400x300")
        history_window.transient(self.root)
        history_window.grab_set()

        # History text widget with scrollbar
        frame = ttk.Frame(history_window, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Text widget with scrollbar
        text_widget = tk.Text(frame, height=15, width=50, font=("Courier", 10))
        scrollbar = ttk.Scrollbar(
            frame, orient=tk.VERTICAL, command=text_widget.yview
        )
        text_widget.configure(yscrollcommand=scrollbar.set)

        # Insert history
        text_widget.insert(tk.END, "Calculation History:\n")
        text_widget.insert(tk.END, "=" * 40 + "\n\n")

        for i, calc in enumerate(history, 1):
            text_widget.insert(tk.END, f"{i:2d}. {calc}\n")

        text_widget.configure(state="disabled")  # Make read-only

        # Grid layout
        text_widget.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        # Clear history button
        clear_btn = ttk.Button(
            frame,
            text="Clear History",
            command=lambda: self.clear_history(history_window),
        )
        clear_btn.grid(row=1, column=0, pady=(10, 0))

        # Configure grid weights
        history_window.columnconfigure(0, weight=1)
        history_window.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

    def clear_history(self, history_window):
        """Clear calculation history."""
        self.calculator.clear_history()
        history_window.destroy()
        messagebox.showinfo(
            "History Cleared", "Calculation history has been cleared."
        )

    def update_display(self, value):
        """Update the calculator display."""
        # Limit display length
        if len(str(value)) > 20:
            # Use scientific notation for very long numbers
            try:
                float_value = float(value)
                if abs(float_value) >= 1e15 or (
                    abs(float_value) < 1e-4 and float_value != 0
                ):
                    value = f"{float_value:.6e}"
                else:
                    value = str(float_value)[:20]
            except (ValueError, TypeError):
                value = str(value)[:20]

        self.display_var.set(str(value))

    def show_error(self, message):
        """Display error message."""
        self.update_display("Error")
        messagebox.showerror("Calculator Error", message)
        self.clear()


def main():
    """Launch the calculator GUI application."""
    root = tk.Tk()
    CalculatorGUI(root)

    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\nCalculator GUI closed.")


if __name__ == "__main__":
    main()
