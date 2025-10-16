# -*- coding: utf-8 -*-
"""
@author: Hamideh
created: Tues Oct 7 13:07:20 2025

Program Description:
-------------------------
Demonstration of Python Dictionary (dict) Data Type and Its Properties
✔ Dictionaries are Mutable → values can be changed after creation.
✔ Store data as key–value pairs → {"key": value}
✔ Keys must be unique and immutable (e.g., str, int, tuple).
✔ Common Methods: keys(), values(), items(), get(), update(), pop(), popitem(), clear(), copy()
✔ Supports nesting (dict within dict).
✔ Great for structured or labeled data.
"""

# --- Dictionary Basics ---
person = {
    "name": "Hamideh",
    "age": 39,
    "city": "Berlin",
    "skills": ["Python", "Control Systems", "Embedded Design"]
}

print("Original Dictionary:", person)
print("Access by key (name):", person["name"])
print("Access with get():", person.get("city"))

# --- Mutability (Change and Add Data) ---
print("\n--- Mutability ---")
person["age"] = 40  # Modify value
person["job"] = "Engineer"  # Add new key-value pair
print("Modified Dictionary:", person)

# --- Common Dictionary Methods ---
print("\n--- Common Dictionary Methods ---")
print("Keys:", list(person.keys()))
print("Values:", list(person.values()))
print("Items:", list(person.items()))

# Update dictionary with another dict
person.update({"hobby": "Reading", "city": "Hamburg"})
print("After update():", person)

# Remove items
removed_city = person.pop("city")   # Remove by key
print("After pop('city'):", person)
print("Removed city value:", removed_city)

last_item = person.popitem()  # Remove last inserted pair
print("After popitem():", person)
print("Removed (key, value):", last_item)

# Copy vs Reference
copy_dict = person.copy()
ref_dict = person
person["language"] = "English"

print("\n--- Copy vs Reference ---")
print("Original:", person)
print("Copy:", copy_dict)  # Independent copy
print("Reference:", ref_dict)  # Same object as person

# --- Nested Dictionaries ---
print("\n--- Nested Dictionary ---")
students = {
    "S1": {"name": "Alice", "age": 23},
    "S2": {"name": "Bob", "age": 25},
    "S3": {"name": "Charlie", "age": 22}
}

print("All Students:", students)
print("Access student S2 name:", students["S2"]["name"])
students["S2"]["age"] = 26  # Modify nested value
print("Modified Nested Dict:", students)
