# -*- coding: utf-8 -*-
"""
skyline.py

Created on Thu Jun 19 14:11:19 2025
@author: Hamideh

This script finds the tallest building (maximum number)
from a list of input heights provided by the user.
"""

def skyline(*args):
    """
    Return the maximum value (tallest height) among the given numbers.

    Args:
        *args: Variable number of numeric arguments.

    Returns:
        int or float: The maximum value among the inputs.
                      Returns None if no arguments are provided.
    """
    if not args:
        return None

    max_height = args[0]
    for height in args[1:]:
        if height > max_height:
            max_height = height
    return max_height


def main():
    """Main entry point of the script."""
    try:
        user_input = input("Enter building heights separated by spaces: ").strip()
        if not user_input:
            print("No input provided.")
            return

        numbers = list(map(float, user_input.split()))
        tallest = skyline(*numbers)
        print(f"The tallest building has a height of: {tallest}")

    except ValueError:
        print("Error: Please enter valid numeric values only.")


if __name__ == "__main__":
    main()
