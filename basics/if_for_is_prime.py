# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 15:45:13 2025

@author: hamid

prime_numbers.py
----------------
Finds all prime numbers up to 1,000,000 and prints
the count and the last prime number found.
"""

import math


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Parameters
    ----------
    n : int
        The number to check.

    Returns
    -------
    bool
        True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    # Only check up to the square root of n
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def main() -> None:
    """Calculate and print prime statistics up to 1,000,000."""
    prime_count = 0
    last_prime_number = 0

    for i in range(1, 1_000_001):
        if is_prime(i):
            last_prime_number = i
            prime_count += 1

    print("\n")
    print(f"We have {prime_count} prime numbers.")
    print(f"The last prime number is {last_prime_number}.")


if __name__ == "__main__":
    main()
