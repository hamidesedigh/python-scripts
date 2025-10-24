# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 23:38:43 2025

@author: hamideh

Problem 1: Multiples of 3 or 5
---------------------------------------------------------------------------------
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6, and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below a given number.
"""


def sum_of_multiples(limit: int) -> int:
    """
    Returns the sum of all natural numbers below 'limit' that are multiples of 3 or 5.

    Parameters:
        limit (int): The upper bound (exclusive) to check multiples.

    Returns:
        int: Sum of multiples of 3 or 5 below 'limit'.
    """
    return sum(i for i in range(1, limit) if i % 3 == 0 or i % 5 == 0)


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        if number <= 0:
            raise ValueError("Number must be a positive integer.")
        total = sum_of_multiples(number)
        print(f"Sum of all multiples of 3 or 5 below {number} is {total}")
    except ValueError as e:
        print(f"Invalid input: {e}")
