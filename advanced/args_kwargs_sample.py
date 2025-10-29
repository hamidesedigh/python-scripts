# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 19:53:07 2025
@author: hamid
"""

def greet(*args, **kwargs):
    # *args collects extra positional arguments as a tuple
    # **kwargs collects extra keyword arguments as a dictionary
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)

    # Example usage
    for name in args:
        print(f"Hello, {name}!")

    if "greeting" in kwargs:
        print(kwargs["greeting"])
    if "punctuation" in kwargs:
        print("Punctuation used:", kwargs["punctuation"])

# Example calls
greet("Alice", "Bob", greeting="Welcome to Python!", punctuation="😊")
