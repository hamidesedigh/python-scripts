# -*- coding: utf-8 -*-
"""
@author: Hamideh
created: Wed Oct 8 6:55:00 2025

Program Description:
-------------------------
Demonstration of Python Tuple, Set, and Boolean Data Types
✔ Tuple → Immutable and Ordered collection.
✔ Set → Mutable, Unordered, No Duplicates.
✔ Boolean → Logical True/False with comparison and logical operators.
"""

# ============================================================
# --- Tuple ---
# ============================================================

print("\n--- Tuple Section ---")
coordinates = (10.5, 20.5, 30.5)
colors = ("red", "green", "blue", "green")  # duplicates allowed
single_item = ("apple",)  # Must include comma for single-element tuple

print("Tuple (coordinates):", coordinates)
print("Tuple (colors):", colors)
print("Single-element tuple:", single_item)
print("Type check:", type(single_item))

# Indexing and slicing
print("First color:", colors[0])
print("Last two colors:", colors[-2:])
print("Repetition:", coordinates * 2)

# Immutability test
# colors[0] = "yellow"  # ❌ Raises TypeError
new_colors = colors + ("yellow",)  # ✅ Create a new tuple
print("Extended tuple:", new_colors)

# Tuple unpacking
x, y, z = coordinates
print("Unpacked coordinates:", x, y, z)

# Tuple methods
print("Count of 'green':", colors.count("green"))
print("Index of 'blue':", colors.index("blue"))

# Quick Summary for Tuple
"""
Quick Summary (Tuple):
----------------------
✔ Immutable → cannot be modified after creation.
✔ Ordered and allows duplicates.
✔ Supports indexing, slicing, and unpacking.
✔ Common methods: count(), index().
✔ Often used for fixed collections or return values.
"""

# ============================================================
# --- Set ---
# ============================================================

print("\n--- Set Section ---")
fruits = {"apple", "banana", "cherry", "apple"}
print("Original Set (duplicates removed):", fruits)

# Mutability and basic operations
fruits.add("orange")
print("After add():", fruits)
fruits.remove("banana")
print("After remove('banana'):", fruits)

# Set operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("\nSet A:", A)
print("Set B:", B)
print("Union (A | B):", A | B)
print("Intersection (A & B):", A & B)
print("Difference (A - B):", A - B)
print("Symmetric Difference (A ^ B):", A ^ B)

# Frozenset example
frozen_A = frozenset(A)
print("Frozen set (immutable):", frozen_A)

# Quick Summary for Set
"""
Quick Summary (Set):
--------------------
✔ Mutable and Unordered collection → No duplicates.
✔ Common methods: add(), remove(), update(), clear().
✔ Mathematical operations: union(|), intersection(&), difference(-), symmetric difference(^).
✔ frozenset → immutable version of set, can be used as dict keys.
✔ Great for membership testing and unique collections.
"""

# ============================================================
# --- Boolean ---
# ============================================================

print("\n--- Boolean Section ---")
is_ready = True
is_empty = False

print("Boolean values:", is_ready, is_empty)
print("Type check:", type(is_ready))

# Comparison operations
a, b = 10, 5
print("a > b:", a > b)
print("a == b:", a == b)
print("a != b:", a != b)

# Logical operations
print("(a > b) and (b < 20):", (a > b) and (b < 20))
print("(a > b) or (b > 20):", (a > b) or (b > 20))
print("not(a > b):", not(a > b))

# Boolean conversion
print("bool(0):", bool(0))
print("bool(1):", bool(1))
print("bool(''):", bool(''))
print("bool('Python'):", bool('Python'))
print("bool([]):", bool([]))
print("bool([1, 2]):", bool([1, 2]))

# Quick Summary for Boolean
"""
Quick Summary (Boolean):
------------------------
✔ Represents logical values → True or False.
✔ Result of comparison and logical expressions.
✔ Common operators: and, or, not.
✔ Any non-zero or non-empty object → True.
✔ 0, None, empty string/list/dict/set → False.
✔ Useful in conditional and loop statements.
"""

# ============================================================
# --- End of Program ---
# ============================================================
print("\nAll sections (Tuple, Set, Boolean) demonstrated successfully.")
