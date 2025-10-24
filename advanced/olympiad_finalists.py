# -*- coding: utf-8 -*-
"""
Created on Tue Sep 9 06:04:46 2025
@author: Hamideh

Description:
------------
This program processes a list of finalists for a Computer Olympiad and prepares
standardized entry cards for the results committee.

Each input record includes:
    - Gender
    - Name (in a non-standard format)
    - Programming language

The input format uses a dot ('.') as a separator between fields. The program:
1. Reads the number of participants.
2. Reads each participant’s record and capitalizes their name properly.
3. Sorts the records first by gender and then by name.
4. Prints a standardized list including gender, name, and language.

Example Input:
--------------
4
female.sara.python
male.ali.cpp
female.lina.java
male.reza.python

Example Output:
---------------
female Lina java
female Sara python
male Ali cpp
male Reza python
"""

def main():
    """Reads participant data, standardizes names, sorts records, and prints results."""

    # Read the number of participants
    cnt = int(input().strip())
    people_list = []

    # Read and process each record
    for _ in range(cnt):
        data = input().strip().split('.')
        data[1] = data[1].capitalize()  # Standardize name capitalization
        people_list.append(data)

    # Sort first by gender, then by name
    sorted_list = sorted(people_list, key=lambda x: (x[0], x[1]))

    # Print standardized output
    for record in sorted_list:
        print(f"{record[0]} {record[1]} {record[2]}")


if __name__ == "__main__":
    main()
