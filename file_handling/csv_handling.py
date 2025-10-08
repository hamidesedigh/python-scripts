# -*- coding: utf-8 -*-
"""
@author: Hamideh
Created on Wed Oct  8 09:53:22 2025

Program Description:
-------------------------
Demonstration of CSV File Handling in Python
--------------------------------------------------------------
Covers:
✔ csv.reader() / csv.writer() : Reads/writes each row of a CSV file as a list of values
✔ DictReader / DictWriter     : Reads/writes each row as a dictionary
✔ Filtering, iteration, and row modification
✔ Simple product project: total price calculation
"""

import csv
from statistics import mean
# ============================================================
# --- Step 1: Create and Write CSV File ---
# ============================================================

csv_file = "people_data.csv"

with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City", "Income"])
    writer.writerow(["Hamideh", 39, "Berlin", 75000])
    writer.writerow(["Ali", 34, "Tehran", 56000])
    writer.writerow(["Sara", 29, "Paris", 61000])
    writer.writerow(["John", 45, "London", 82000])
    writer.writerow(["Mary", 31, "Berlin", 72000])

print("✅ 'people_data.csv' created successfully.\n")

# ============================================================
# --- Step 2: Read CSV using csv.reader() ---
# ============================================================

print("--- Reading with csv.reader() ---")
with open(csv_file, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# ============================================================
# --- Step 3: Read CSV using DictReader ---
# ============================================================

print("\n--- Reading with DictReader ---")
people = []
with open(csv_file, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["Age"] = int(row["Age"])
        row["Income"] = int(row["Income"])
        people.append(row)
        print(row)

# ============================================================
# --- Step 4: Filter Data and Save to New CSV ---
# ============================================================
average_age = mean(p["Age"] for p in people)
average_income = mean(p["Income"] for p in people)
berlin_people = [p for p in people if p["City"] == "Berlin"]

print("\n📊 Data Analysis:")
print(f"Average Age: {average_age:.1f}")
print(f"Average Income: €{average_income:,.0f}")
print(f"People in Berlin: {len(berlin_people)}")

filtered_csv = "berlin_people.csv"
with open(filtered_csv, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=people[0].keys())
    writer.writeheader()
    writer.writerows(berlin_people)

print(f"\n✅ Filtered Berlin people saved to '{filtered_csv}'.")

# ============================================================
# --- Step 5: Mini Project – Product CSV Calculator ---
# ============================================================

print("\n🛒 Mini Project: Calculating Total Price for Products")

product_file = "products.csv"
with open(product_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Quantity", "Unit Price"])
    writer.writerow(["Keyboard", 5, 20])
    writer.writerow(["Mouse", 10, 8])
    writer.writerow(["Monitor", 2, 150])
    writer.writerow(["USB Cable", 12, 5])

# --- Process and calculate totals ---
with open(product_file, encoding="utf-8") as file:
    csv_data = csv.reader(file)
    lines = list(csv_data)

new_lines = []
for line in lines:
    new_line = list(line)
    if line[0] == 'Product Name':
        new_line.append('Total Price')
    else:
        total = int(line[1]) * int(line[2])
        new_line.append(str(total))
    new_lines.append(new_line)

print("\nProcessed Product Data:")
for line in new_lines:
    print(line)

# --- Save results ---
out_file = "outProducts.csv"
with open(out_file, mode="w", newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile, delimiter=',')
    writer.writerows(new_lines)

print(f"✅ Calculated totals saved to '{out_file}'")

# ============================================================
# --- Quick Summary ---
# ============================================================
"""
Quick Summary:
--------------
✔ csv.reader()/writer() → Basic file reading/writing
✔ DictReader/DictWriter → Works with column names
✔ Data can be filtered and saved easily
✔ Project: Calculated total price for each product
"""
