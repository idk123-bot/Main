# games/calculator.py
import logging
import time
from Utils.Helpers import return_to_menu, returnx
from Utils.Screen import clear


def run(name=None):
    """Simple calculator that performs basic operations on two numbers."""
    logging.info("User selected calculator")
    while True:
        try:
            num1_input = (
                input(
                    "What is the first number? (type 'Return' to return to main menu) "
                )
                .strip()
                .lower()
            )

            if returnx(num1_input):
                return

            num1 = float(num1_input)

            op = input("What is the operation (+ - x * /)? ").strip().lower()

            # Get second number based on operation
            if op == "/":
                while True:
                    num2_input = input("What is the second number? ").strip().lower()
                    if returnx(num2_input):
                        return
                    try:
                        num2 = float(num2_input)
                        if num2 == 0:
                            print("Can't divide by zero! Try again.")
                            continue
                        break
                    except ValueError:
                        print("Please enter a valid number!")
            elif op in ["+", "-", "x", "*"]:
                num2_input = input("What is the second number? ").strip().lower()
                if returnx(num2_input):
                    return
                num2 = float(num2_input)
            else:
                print("Please enter a valid operator (+, -, x, *, /)!")
                logging.error(f"User entered invalid operator: {op}")
                time.sleep(2)
                continue

            # Calculate result
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op in ["x", "*"]:
                result = num1 * num2
            elif op == "/":
                result = num1 / num2

            print(f"\nThe Answer is {result:<10.2f}")
            logging.info(f"Calculated result: {num1} {op} {num2} = {result}")

            choice = input("Wanna try do it again (y/n)? ").strip().lower()
            if choice in ["yes", "y"]:
                clear()
                continue
            break

        except ValueError:
            print("Please enter valid numbers!")
            logging.error("User entered invalid numbers for calculation")
            continue
