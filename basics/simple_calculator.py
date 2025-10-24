# -*- coding: utf-8 -*-
'''
Created on Tue Jun 17 23:38:43 2025
@author: hamideh

Simple Calculator Program
'''

def add(x: float, y: float) -> float:
    """Return the sum of x and y."""
    return x + y

def subtract(x: float, y: float) -> float:
    """Return the difference of x and y."""
    return x - y

def multiply(x: float, y: float) -> float:
    """Return the product of x and y."""
    return x * y

def divide(x: float, y: float) -> float | str:
    """Return the division of x by y. Return error message if dividing by zero."""
    if y != 0:
        return x / y
    return "Error: Division by zero"

def get_number(prompt: str) -> float:
    """Prompt user to input a number, retry until valid."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ").strip()
        if choice not in ('1', '2', '3', '4'):
            print("Invalid choice. Please select a valid option.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        operations = {
            '1': (add, '+'),
            '2': (subtract, '-'),
            '3': (multiply, '*'),
            '4': (divide, '/')
        }

        func, symbol = operations[choice]
        result = func(num1, num2)
        print(f"{num1} {symbol} {num2} = {result}")

        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    calculator()
