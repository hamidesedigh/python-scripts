# -*- coding: utf-8 -*-
"""
Created on Sun Aug 10 10:14:37 2025

Write a program that reads 10 integers from input.
At the end, the program should print the number that has the largest number of distinct prime divisors, along with that count.
If multiple numbers have the same maximum count, print the largest number among them.

Example Input:
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
678 3
@author: hamid
"""
def is_prime(n):
    if n < 2:
        return False
    # optimize the loop
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def prime_divisors_count(n):
    count = 0
    # count the number of prime gcd
    for i in range(2, n+1):
        if n % i == 0 and is_prime(i):
            count += 1
    return count

def main():
    # Read how many numbers you will input
    cnt = 10
    numbers = [int(input().strip()) for _ in range(cnt)]
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