# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 06:24:18 2025
@author: Hamideh

Program Description:
--------------------
This program validates an email address using regular expressions.

Rules:
- The email must follow the format: expression@string.string
  (e.g., user123@gmail.com)
- The expression (username) can include letters, digits, dots, underscores, or hyphens.
- The domain must include at least one dot (e.g., gmail.com, yahoo.co.uk).

Output:
- Prints "OK" if the email is valid.
- Prints "WRONG" if the email does not match the pattern.
"""

import re

def is_valid_email(email):
    """
    Checks if the given email matches the pattern expression@string.string
    """
    # Updated pattern to allow common characters and subdomains
    pattern = r'^[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.match(pattern, email) is not None


def main():
    """
    Reads an email address from user input and validates it.
    """
    email = input("Enter your email address: ").strip()
    if is_valid_email(email):
        print("OK")
    else:
        print("WRONG")


if __name__ == "__main__":
    main()
