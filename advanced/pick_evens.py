# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 10:35:49 2025
@author: Hamideh

A simple program that reads a list of integers from the user
and returns only the even numbers.
"""


def pick_evens(*args):
    """
    Return a list of even numbers from the given arguments.

    Args:
        *args: Variable number of integer inputs.

    Returns:
        list[int]: A list containing only the even numbers.
    """
    return [num for num in args if num % 2 == 0]


def main():
    """Main entry point for the script."""
    try:
        # Read user input
        user_input = input("Enter numbers separated by spaces: ").strip()
        if not user_input:
            print("No input provided.")
            return

        # Convert input to integers
        numbers = list(map(int, user_input.split()))

        # Print the even numbers
        evens = pick_evens(*numbers)
        print("Even numbers:", evens)

    except ValueError:
        print("Error: Please enter valid integers only.")


if __name__ == "__main__":
    main()
