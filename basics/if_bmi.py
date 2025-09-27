# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 20:15:32 2025

@author: hamid
"""

# BMI Calculator
weight = 75  # in kilograms
height = 180 / 100  # convert height to meters

# BMI formula
bmi = weight / height**2

print(f"Your BMI is: {bmi:.2f}")  # show BMI rounded to 2 decimal places

if bmi < 18.5:
    print("You are underweight!")
elif 18.5 <= bmi <= 24.9:
    print("You have a healthy weight!")
else:
    print("You are overweight!")