# -*- coding: utf-8 -*-
"""
Created on Sun Aug 10 10:14:37 2025
@author: Hamideh

Description:
------------
This program reads 10 integers from input and identifies the number that has
the largest number of distinct prime divisors. If multiple numbers have the
same maximum count of distinct prime divisors, the largest number among them
is chosen.

Functions:
----------
- is_prime(n): Checks whether a given number n is prime.
- prime_divisors_count(n): Counts the number of distinct prime divisors of n.

Example Input:
--------------
123
43
54
12
76
84
98
678
543
231

Example Output:
---------------
678 3
"""

def is_prime(n: int) -> bool:
    """Check if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_divisors_count(n: int) -> int:
    """Return the number of distinct prime divisors of n."""
    count = 0
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            count += 1
    return count

def main():
    """Main program logic."""
    # Read 10 integers from input
    numbers = [int(input().strip()) for _ in range(10)]

    max_count = -1
    result_number = -1

    for num in numbers:
        cnt = prime_divisors_count(num)
        if cnt > max_count or (cnt == max_count and num > result_number):
            max_count = cnt
            result_number = num

    print(f"{result_number} {max_count}")

if __name__ == "__main__":
    main()
