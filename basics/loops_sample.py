# -*- coding: utf-8 -*-
"""
@author: Hamideh
created: Sat Sep 27 15:45:13 2025

Program Description:
-------------------------
Illustrates Python iteration techniques over different data structures:
✔ Strings (character iteration and enumerate)
✔ Dictionaries (key-value pairs and indexed iteration)
✔ Ranges (basic looping)
✔ Lists (using enumerate for index-value pairs)
"""

def iterate_string(word: str) -> None:
    """Iterate over each character in a string."""
    print("Iterating over a string:")
    for char in word:
        print(char)


def enumerate_string(word: str) -> None:
    """Iterate over a string with index using enumerate."""
    print("Enumerating a string:")
    for index, char in enumerate(word):
        print(f"Index {index}: {char}")


def iterate_dictionary(data: dict) -> None:
    """Iterate over keys and values in a dictionary."""
    print("\nIterating over a dictionary:")
    for key, value in data.items():
        print(f"Key: {key}, Value: {value}")


def enumerate_dict(data: dict) -> None:
    """Iterate over a dictionary with index using enumerate on keys."""
    print("\nEnumerating a dictionary (keys):")
    for index, key in enumerate(data):
        print(f"Index {index}: Key={key}, Value={data[key]}")


def iterate_range(n: int) -> None:
    """Iterate over a range of numbers."""
    print("\nIterating over a range:")
    for number in range(n):
        print(number)


def enumerate_list(items: list) -> None:
    """Iterate over a list with index using enumerate."""
    print("\nEnumerating a list:")
    for index, value in enumerate(items):
        print(f"Index {index}: {value}")


def main() -> None:
    """Main function to run iteration examples."""
    iterate_string("Python")
    iterate_dictionary({"name": "Alice", "age": 30, "city": "Berlin"})
    iterate_range(5)

    """Main function to run enumerate examples."""
    enumerate_string("C programming")
    enumerate_list(["apple", "banana", "cherry"])
    enumerate_dict({"name": "Alice", "age": 30, "city": "Berlin"})


if __name__ == "__main__":
    main()
