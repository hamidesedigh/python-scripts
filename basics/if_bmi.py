# -*- coding: utf-8 -*-
"""
@author: Hamideh
created: Wed Sep 24 20:15:32 2025

Program Description:
-------------------------
Body Mass Index (BMI) Calculator

This script calculates a person's BMI based on weight (kg)
and height (cm → converted to meters). It then classifies
the BMI result according to standard WHO categories:
- Underweight: < 18.5
- Normal weight: 18.5 – 24.9
- Overweight: ≥ 25
--------------------------------------------------------------
Formula:
    BMI = weight (kg) / (height (m))²
"""

# ============================================================
# --- Step 1: Define Input Data ---
# ============================================================

# Option A: Static values
weight = 75   # in kilograms
height_cm = 180  # height in centimeters

# Option B (uncomment for dynamic user input)
# weight = float(input("Enter your weight (kg): "))
# height_cm = float(input("Enter your height (cm): "))

# Convert height to meters
height_m = height_cm / 100

# ============================================================
# --- Step 2: Compute BMI ---
# ============================================================

bmi = weight / (height_m ** 2)

# ============================================================
# --- Step 3: Display and Categorize Result ---
# ============================================================

print(f"\nYour BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("🔹 You are underweight.")
elif 18.5 <= bmi <= 24.9:
    print("✅ You have a healthy weight.")
elif 25 <= bmi <= 29.9:
    print("⚠️ You are overweight.")
else:
    print("❗ You are obese.")