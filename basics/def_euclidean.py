# -*- coding: utf-8 -*-
"""
@author: Hamideh
created: Wed Sep 24 20:23:20 2025

Program Description:
-------------------------
Implementation of the Euclidean Algorithm to compute the
Greatest Common Divisor (GCD) of two integers.

The Euclidean method repeatedly replaces the larger number
with the remainder of dividing the larger by the smaller
until the remainder becomes zero.
--------------------------------------------------------------
Formula:
    gcd(a, b) = gcd(b, a % b)
Example:
    gcd(12, 18) → 6
"""

def euclidean_method(a: int, b: int) -> int:
    """
    Compute the Greatest Common Divisor (GCD) of two integers
    using the Euclidean algorithm.

    Parameters:
        a (int): First number
        b (int): Second number

    Returns:
        int: The GCD of the two numbers
    """
    # Ensure a is the larger number
    a, b = max(a, b), min(a, b)

    # Repeat until remainder is zero
    while b != 0:
        a, b = b, a % b  # Replace (a, b) → (b, remainder)

    return a


# ============================================================
# --- Example Usage ---
# ============================================================

if __name__ == "__main__":
    print("✅ Euclidean GCD Examples:")
    print(f"gcd(12, 18) = {euclidean_method(12, 18)}")   # Expected output: 6
    print(f"gcd(42, 56) = {euclidean_method(42, 56)}")   # Expected output: 14
    print(f"gcd(270, 192) = {euclidean_method(270, 192)}")  # Expected output: 6
