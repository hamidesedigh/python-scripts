# -*- coding: utf-8 -*-
"""
@author: Hamideh
created: Tues Oct 7 10:07:20 2025

Program Description:
-------------------------
Demonstration of Python List Data Type and Its Properties
✔ Lists are Mutable → can modify elements directly.
✔ Ordered → maintain insertion order.
✔ Allow Duplicates → [1, 1, 2] is valid.
✔ Indexable & Sliceable.
✔ Common Methods: append(), insert(), extend(), remove(), pop(), sort(), reverse(), count(), index()
✔ del(my_list)
✔ Can contain mixed data types.
✔ Support nesting and shallow/deep copies.
"""

# --- List Basics ---
numbers = [10, 20, 30, 40, 50]
fruits = ["apple", "banana", "cherry", "kiwi"]
mixed = [1, "hello", 3.5, True]

print("Numbers List:", numbers)
print("Fruits List:", fruits)
print("Mixed Data Types:", mixed)

# --- Indexing and Slicing ---
print("\n--- Indexing & Slicing ---")
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Slice fruits[1:3]:", fruits[1:3])
print("Every 2nd number:", numbers[::2])

# --- Mutability ---
print("\n--- Mutability ---")
fruits[1] = "orange"   # Modify element
print("Modified Fruits:", fruits)
fruits.append("melon")  # Add new element at end
print("After append:", fruits)

# --- Common List Methods ---
print("\n--- Common List Methods ---")
numbers.append(60)
print("Append:", numbers)

numbers.insert(2, 25)
print("Insert at index 2:", numbers)

numbers.remove(40)
print("Remove element 40:", numbers)

popped_item = numbers.pop()
print("Pop last element:", popped_item, "| New list:", numbers)

print("Count of 20:", numbers.count(20))
print("Index of 30:", numbers.index(30))

numbers.sort()
print("Sorted List:", numbers)

numbers.reverse()
print("Reversed List:", numbers)

# --- Nested Lists ---
print("\n--- Nested Lists ---")
matrix = [[1, 2], [3, 4], [5, 6]]
print("Matrix:", matrix)
print("Access matrix[1][0]:", matrix[1][0])  # Access nested element

# --- Copying Lists (Shallow vs Deep) ---
print("\n--- Copying Behavior ---")
a = [1, 2, 3]
b = a                # Reference copy (same memory)
c = a.copy()         # Shallow copy (new memory)

a.append(4)
print("Original (a):", a)
print("Reference copy (b):", b)
print("Independent copy (c):", c)
