# -*- coding: utf-8 -*-
"""
@author: Hamideh
created: Mon Oct 6 15:23:20 2025

Program Description:
-------------------------
Demonstration of Python String Data Type and Its Properties
✔ Strings are Immutable → cannot be changed after creation.
✔ Support Indexing & Slicing.
✔ Common Methods: upper(), lower(), replace(), split(), count().
✔ String Formatting Options:
   1. Concatenation → "Hello " + name
   2. Old-style (%) → "Hello %s" % name
   3. str.format() → "Hello {}".format(name)
   4. f-strings → f"Hello {name}"
"""

# --- String Basics ---
text = "Hello Python!"
print("Original String:", text)

# Indexing and slicing
print("First character:", text[0])
print("Substring [7:-1]:", text[7:-1])
print("Every 2nd character [::2]:", text[::2])
print("Reversed [::-1]:", text[::-1])

# Strings are immutable — cannot modify directly
new_text = "X" + text[1:]
print("\nModified string (by creating new one):", new_text)

# --- Common String Methods ---
print("\n--- String Methods ---")
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Replace 'Python' with 'World':", text.replace("Python", "World"))
print("Split by comma:", text.split(","))
print("Count of 'l':", text.count("l"))

# --- String Interpolation / Formatting ---
print("\n--- String Interpolation ---")
name = "Hamideh"
family_name = "Sedigh"
age = 39

# Different formatting styles
print("Concatenation:", "Hello " + name + " " + family_name)
print("C-style (%):", "Hello %s %s, you are %i" % (name, family_name, age))
print("format() method:", "Hello {} {}, you are {}".format(name, family_name, age))
print("Named placeholders:", "Hello {name} {family}, you are {sen:1.1f}".format(
    name=name, family=family_name, sen=age))
print(f"f-string:", f"Hello {name} {family_name}, you are {age:1.1f}")



