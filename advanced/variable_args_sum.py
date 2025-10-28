# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 10:26:32 2025
@author: Hamideh

A simple script demonstrating the use of *args to sum
any number of numeric inputs provided by the user.
"""


def sum_numbers(*args):
    """
    Calculate the sum of any number of input numbers.

    Args:
        *args: Variable number of numeric arguments.

    Returns:
        int | float: Sum of all input numbers.
    """
    total = 0
    for num in args:
        total += num
    return total


def main():
    """Main entry point for the script."""
    try:
        # Read space-separated numbers from user input
        user_input = input("Enter numbers separated by spaces: ").strip()
        if not user_input:
            print("No input provided.")
            return

        # Convert input string to list of integers
        numbers = list(map(int, user_input.split()))

        # Calculate and print the sum
        total = sum_numbers(*numbers)
        print("Sum:", total)

    except ValueError:
        print("Error: Please enter only valid integers.")


if __name__ == "__main__":
    main()
