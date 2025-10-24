# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 19:27:33 2025
@author: hamideh

Utility functions for basic mathematical operations.
"""
import math

def factorial(n):
    """Return factorial of n using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return 1 if n in (0, 1) else n * factorial(n - 1)

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def average(numbers):
    """Return the average of a list of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0

def main():
    print(factorial(5))  # 120
    print(is_prime(7))  # True
    print(average([2, 4]))  # 3.0


if __name__ == '__main__':
    main()