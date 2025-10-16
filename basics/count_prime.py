# -*- coding: utf-8 -*-
"""
@author: Hamideh
Created on Sat Sep 27 15:45:13 2025

Description
-----------
Efficiently finds all prime numbers up to 1,000,000
and prints both the total count and the last prime number found.

This script demonstrates:
- Basic algorithm optimization (√n primality check)
- Loop iteration efficiency with integer square roots
- Structured and readable code with docstrings

Example
-------
$ python prime_numbers.py

Output:
--------
We have 78498 prime numbers.
The last prime number is 999983.
"""

import math


# ============================================================
# --- Prime Number Check Function ---
# ============================================================

def is_prime(n: int) -> bool:
    """
    Determine if a given number is prime.

    Parameters
    ----------
    n : int
        The number to be tested.

    Returns
    -------
    bool
        True if `n` is prime, otherwise False.
    """
    if n < 2:
        return False
    if n == 2:  # handle 2 early (even and prime)
        return True
    if n % 2 == 0:
        return False  # exclude other even numbers

    # Check only odd divisors up to √n
    limit = int(math.isqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True


# ============================================================
# --- Main Computation Function ---
# ============================================================

def main() -> None:
    """
    Compute and print the count and last prime number up to 1,000,000.
    """
    prime_count = 0
    last_prime_number = 0

    for i in range(2, 1_000_001):
        if is_prime(i):
            prime_count += 1
            last_prime_number = i

    print("\n--- Prime Number Statistics ---")
    print(f"✅ Total primes found: {prime_count}")
    print(f"🔹 Last prime number: {last_prime_number}")


# ============================================================
# --- Script Entry Point ---
# ============================================================

if __name__ == "__main__":
    main()
