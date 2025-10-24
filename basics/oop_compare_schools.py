# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 06:11:13 2025
@author: hamideh

Program Description:
--------------------
This program compares two schools (A and B) based on student statistics 
(age, height, weight). It calculates the average values of these attributes 
for each school, prints them, and then determines which school is "better" 
based on average height and weight.

Input:
    5
    16 17 15 16 17
    180 175 172 170 165
    67 72 59 62 55
    5
    15 17 16 15 16
    166 156 168 170 162
    45 52 56 58 47
Output:
    16.2
    172.4
    63.0
    15.8
    164.4
    51.6
    A

"""
import numpy as np

class School:
    
    # Represents a school with student statistics such as age, height, and weight.

    milk_sch = 'True' # Class attribute, shared across all schools unless overridden

    def __init__(self, age, height, weight):
        
        # Initialize the School object with arrays of age, height, and weight.
        
        self.age = age
        self.height = height
        self.weight = weight
    def average_age(self):
        # Return the average age of students in the school.
        return float(self.age.mean())
    
    def average_height(self):
        # Return the average height of students in the school.
        return float(self.height.mean())
    
    def average_weight(self):
        # Return the average weight of students in the school.
        return float(self.weight.mean())

def listed_num(n):
    # Reads a line of space-separated integers from input,
    # converts them into a NumPy array, and returns the first n elements.
    
    line = input().strip()
    parts = [int(x) for x in line.split()]
    listed_ = np.array(parts)
    return listed_[:n]


# ==============================
# Main Program Execution
# ==============================

# Input for School A
num_A = int(input())
age_A = listed_num(num_A)
height_A = listed_num(num_A)
weight_A = listed_num(num_A)

# Input for School B
num_B = int(input())
age_B = listed_num(num_B)
height_B = listed_num(num_B)
weight_B = listed_num(num_B)

# Create School objects
sch_A = School(age_A, height_A, weight_A)
sch_B = School(age_B, height_B, weight_B)
sch_B.milk_sch = 'False' # Override class attribute for School B

# Print average statistics
print(sch_A.average_age())
print(sch_A.average_height())
print(sch_A.average_weight())

print(sch_B.average_age())
print(sch_B.average_height())
print(sch_B.average_weight())


# Comparison Logic
if sch_A.average_height() > sch_B.average_height():
    print('A')
elif sch_A.average_height() == sch_B.average_height():
    if sch_A.average_weight() > sch_B.average_weight():
        print('B')
    elif sch_A.average_weight() == sch_B.average_weight():
        print('Same')
    else:
        print('A')
else:
    print('B')

