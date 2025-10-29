# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 20:41:53 2025
@author: hamid
"""

# A list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ✅ 1. Use filter() with a lambda to select even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# ✅ 2. Use map() with a lambda to square each number
squared_numbers = list(map(lambda x: x ** 2, numbers))

# ✅ 3. Combine filter() and map(): square only even numbers
squared_evens = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))

# ✅ 4. Display results
print("Original list:     ", numbers)
print("Even numbers:      ", even_numbers)
print("Squared numbers:   ", squared_numbers)
print("Squared even nums: ", squared_evens)
