# -*- coding: utf-8 -*-
"""
@author: Hamideh
@created: Wed Oct 6 15:23:20 2025

Program Description:
-------------------------
Demonstration of Basic Python Data Types and Their Properties
--------------------------------------------------------------
Covers:
- Numeric, Sequence, Mapping, Set, Boolean, Binary, NoneType
- Mutability, Order, and Example Operations
- Operator Precedence
"""

# ==============================================================
# 1️⃣ Numeric Types → int, float, complex
# ❌ Mutable, ❌ Ordered
# Operator precedence: () → ** → * / // % → + -
# ==============================================================

a = 5           # int
b = 3.14        # float
c = 2 + 3j      # complex

print("Integer:", a)
print("Float:", b)
print("Complex:", c)
print()

# ==============================================================
# 2️⃣ Sequence Types → str, list, tuple, range
# ✅ list (mutable), ❌ tuple & str (immutable), ✅ Ordered
# ==============================================================

# --- String ---
text = "Hello Python!"
print("String:", text)
print("First character:", text[0])
print("Substring:", text[7:-1])
print("Every 2nd character:", text[::2])
print("Reversed:", text[::-1])
print()

# --- List ---
fruits = ["apple", "banana", "cherry"]
print("List of fruits:", fruits)
fruits.append("orange")
fruits[1] = "kiwi"
print("Modified list of fruits:", fruits)
print("List of fruits:", fruits)
print("Sliced list:", fruits[1:3])
print("List length:", len(fruits))
print()

# --- Tuple ---
coordinates = (10.5, 20.5)
print("Tuple:", coordinates)
print("Tuple slicing:", coordinates[:2])
# coordinates[0] = 100  # ❌ Immutable
print()

# --- Range ---
rng = range(5)
print("Range:", list(rng))
print()

# ==============================================================
# 3️⃣ Mapping Type → dict
# ✅ Mutable, ✅ Ordered
# ==============================================================

person = {"name": "Alice", "age": 25, "city": "Berlin"}
print("Dictionary:", person)
print("Access value:", person["name"])

# Modify dictionary
person["age"] = 26
person["job"] = "Engineer"

print("Updated dictionary:", person)
print("Keys:", list(person.keys()))
print("Values:", list(person.values()))
print()

# ==============================================================
# 4️⃣ Set Types → set, frozenset
# ✅ set (mutable), ❌ frozenset (immutable), ❌ Ordered
# ==============================================================

unique_nums = {1, 2, 3, 3, 2}  # duplicates auto-removed
print("Set (duplicates removed):", unique_nums)

unique_nums.add(4)
unique_nums.update({5, 6})
unique_nums.remove(1)
print("Modified set:", unique_nums)

frozen = frozenset({1, 2, 3})
print("Frozen set:", frozen)
print()

# ==============================================================
# 5️⃣ Boolean Type → bool
# ❌ Mutable, ❌ Ordered
# ==============================================================

is_valid = True
is_done = False
print("Boolean values:", is_valid, is_done)

a, b = 10, 5
print("a > b:", a > b)
print("a == b:", a == b)
print("Boolean operations:", (a > b) and (b < 20))
print()

# ==============================================================
# 6️⃣ Binary Types → bytes, bytearray, memoryview
# ✅ bytearray (mutable), ❌ bytes & memoryview (immutable), ✅ Ordered
# ==============================================================

data_bytes = b"Hi"
data_bytearray = bytearray(b"Hi")
data_memory = memoryview(b"Hi")

print("Bytes:", data_bytes)
print("Bytearray:", data_bytearray)
print("Memoryview:", data_memory)
print()

# ==============================================================
# 7️⃣ NoneType → None
# ❌ Mutable, ❌ Ordered
# ==============================================================

nothing = None
print("NoneType example:", nothing)
print()

# ==============================================================
# 8️⃣ Type Checking Summary
# ==============================================================

print("Type of fruits:", type(fruits))
print("Type of coordinates:", type(coordinates))
print("Type of nothing:", type(nothing))
print("Type of unique_nums:", type(unique_nums))
print("Type of person:", type(person))
print("Type of (a > b):", type(a > b))
print()

# ==============================================================
# 🧾 Quick Summary of Python Data Categories
# ==============================================================

summary = {
    "Numeric": ["int", "float", "complex"],
    "Sequence": ["str", "list", "tuple", "range"],
    "Mapping": ["dict"],
    "Set": ["set", "frozenset"],
    "Boolean": ["bool"],
    "Binary": ["bytes", "bytearray", "memoryview"],
    "NoneType": ["None"]
}

print("===================================")
print(" Quick Summary of Data Categories")
print("===================================")
for category, types in summary.items():
    print(f"{category}: {', '.join(types)}")

print("\nMutable vs Immutable:")
print("Mutable: list, dict, set, bytearray")
print("Immutable: int, float, str, tuple, frozenset, bool, bytes, NoneType")
