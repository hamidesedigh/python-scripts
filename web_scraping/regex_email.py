# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 06:24:18 2025

@author: hamid

The email must follow the format expression@string.string (e.g., user123@gmail.com).
"""

import re

def is_valid_email(email):
    #Check if email matches expression@string.string

    pattern = r'^[A-Za-z0-9]+@[A-Za-z]+\.[A-Za-z]+$'
    return re.match(pattern, email) is not None

def main():
    email = input().strip()
    if is_valid_email(email):
        print("OK")
    else:
        print("WRONG")

if __name__ == "__main__":
    main()