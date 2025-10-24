# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 21:50:29 2025
@Author: hamideh

PIN Puzzle Solver
-----------------------------------------------------------
This program searches for all 5-digit PIN codes that satisfy
a set of mathematical conditions involving the digits.

Conditions:
1. digit5 + digit3 == 14
2. digit1 == 2 * digit2 - 1
3. digit4 == digit2 + 1
4. digit2 + digit3 == 10
5. Sum of all digits == 30
"""

def pin_is_ok(d1: int, d2: int, d3: int, d4: int, d5: int) -> bool:
    """Check whether a 5-digit PIN satisfies the puzzle constraints."""
    return all([
        d5 + d3 == 14,
        d1 == 2 * d2 - 1,
        d4 == d2 + 1,
        d2 + d3 == 10,
        d1 + d2 + d3 + d4 + d5 == 30
    ])

if __name__ == "__main__":
    for pin in range(100000):
        d1, d2, d3, d4, d5 = map(int, str(pin).zfill(5))
        if pin_is_ok(d1, d2, d3, d4, d5):
            print(f"PIN code is {pin:05d}")
