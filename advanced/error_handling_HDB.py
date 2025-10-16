# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 06:12:23 2025

@author: hamid

Program Description:
--------------------
This program reads a birthdate (format: YYYY/MM/DD), calculates the age 
in years based on today's date, and prints the result. 
If the input format is invalid, it prints an error message.

Input: 1995/02/03
Output: 24
"""

from datetime import datetime, date

# Read birthdate string from user
bd_str = input().strip()

try:
    # Convert string to date object
    bd = datetime.strptime(bd_str, "%Y/%m/%d").date()
    
    # Get today's date
    today = date.today()
    
    # Calculate difference in days
    days = today - bd
    
    # Convert to years (approximate, accounting for leap years)
    age = days/365.25
    
    # Print result 
    print(age.days)
except ValueError:
    # Handles incorrect date format
    print("WRONG ")
    
