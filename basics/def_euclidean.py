# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 20:23:20 2025

@author: hamid
"""

def euclidean_method(a, b):
    """
    Compute the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm.
    """
    # Ensure a >= b
    a, b = max(a, b), min(a, b)
    
    while b != 0:
        a, b = b, a % b  # update numbers
    
    return a

# Example usage
print(euclidean_method(12, 18))  # Output: 6
