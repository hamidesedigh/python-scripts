# -*- coding: utf-8 -*-
"""
Created: Mon Oct 6 15:23:20 2025
@Author: Hamideh

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

# ----------------------------------------------------------------------
# 🔹 Utility Functions
# ----------------------------------------------------------------------
def capitalize_words(sentence):
    """Capitalize the first letter of each word."""
    return " ".join(word.capitalize() for word in sentence.split())


def is_palindrome(s):
    """Check if a string is a palindrome (case-insensitive)."""
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


def word_count(s):
    """Return the number of words in a sentence."""
    return len(s.split())


# ----------------------------------------------------------------------
# 🔹 Demonstration Section
# ----------------------------------------------------------------------
def main():
    # --- String Basics ---
    text = "Hello Python!"
    print("🔹 Original String:", text)
    print("First character:", text[0])
    print("Substring [7:-1]:", text[7:-1])
    print("Every 2nd character [::2]:", text[::2])
    print("Reversed [::-1]:", text[::-1])

    # Strings are immutable — cannot modify directly
    new_text = "X" + text[1:]
    print("\nModified string (created new one):", new_text)

    # --- Common String Methods ---
    print("\n--- 🧩 String Methods ---")
    print("Uppercase:", text.upper())
    print("Lowercase:", text.lower())
    print("Replace 'Python' with 'World':", text.replace("Python", "World"))
    print("Split by comma:", text.split(","))
    print("Count of 'l':", text.count("l"))

    # --- String Interpolation / Formatting ---
    print("\n--- 🎨 String Interpolation ---")
    name = "Hamideh"
    family_name = "Sedigh"
    age = 39

    print("Concatenation:", "Hello " + name + " " + family_name)
    print("C-style (%):", "Hello %s %s, you are %i" % (name, family_name, age))
    print("format() method:", "Hello {} {}, you are {}".format(name, family_name, age))
    print("Named placeholders:",
          "Hello {name} {family}, you are {sen:1.1f}".format(
              name=name, family=family_name, sen=age))
    print(f"f-string: Hello {name} {family_name}, you are {age:1.1f}")

    # --- Utility Function Demonstrations ---
    print("\n--- 🧠 Utility Functions ---")
    print("Capitalize Words:", capitalize_words("hello world"))      # Hello World
    print("Is Palindrome (Madam):", is_palindrome("Madam"))           # True
    print("Word Count ('I love Python'):", word_count("I love Python"))  # 3


# ----------------------------------------------------------------------
# 🔹 Run as Script
# ----------------------------------------------------------------------
if __name__ == "__main__":
    main()
