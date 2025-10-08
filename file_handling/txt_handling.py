# -*- coding: utf-8 -*-
"""
@author: Hamideh
Created on Wed Oct  8 09:35:18 2025

Program Description:
-------------------------
Demonstration of Python File Handling
--------------------------------------------------------------
Covers:
✔ open()       → Open a file in different modes (read, write, append)
✔ read()       → Read the entire file content
✔ readline()   → Read one line at a time
✔ readlines()  → Read all lines into a list
✔ seek()       → Move the file cursor to a specific position
✔ close()      → Close the file manually
✔ with open()  → Context manager (auto close)
"""

# ============================================================
# --- Step 1: Create a sample file for testing ---
# ============================================================

file_name = "sample_text.txt"

with open(file_name, "w", encoding="utf-8") as file:
    file.write("Line 1: Hello, Python!\n")
    file.write("Line 2: File handling is easy.\n")
    file.write("Line 3: You can read, write, and seek.\n")
    file.write("Line 4: Remember to close your file!\n")

print("✅ Sample file created successfully.\n")

# ============================================================
# --- Step 2: Open and Read Entire File ---
# ============================================================

# Open the file in read mode ('r')
f = open(file_name, "r", encoding="utf-8")

# Read the entire content
print("--- Using read() ---")
content = f.read()
print(content)

# Always good to check current cursor position
print("Cursor position after read():", f.tell())

# Move cursor back to the start
f.seek(0)
print("Cursor reset to:", f.tell())

# ============================================================
# --- Step 3: Read Line by Line ---
# ============================================================

print("\n--- Using readline() ---")
f.seek(0)
line1 = f.readline()
line2 = f.readline()
print("First line:", line1.strip())
print("Second line:", line2.strip())

# ============================================================
# --- Step 4: Read All Lines into a List ---
# ============================================================

print("\n--- Using readlines() ---")
f.seek(0)
lines = f.readlines()
print("List of lines:", lines)
print("Total number of lines:", len(lines))

# ============================================================
# --- Step 5: Move Cursor with seek() ---
# ============================================================

print("\n--- Using seek() ---")
f.seek(15)  # Move cursor to 15th character
partial = f.read(20)
print("Reading from position 15:", partial)

# ============================================================
# --- Step 6: Close the File ---
# ============================================================

f.close()
print("\nFile closed manually:", f.closed)

# ============================================================
# --- Step 7: Best Practice - with open() Context Manager ---
# ============================================================

print("\n--- Using 'with open()' ---")
with open(file_name, "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# File auto-closed after leaving 'with' block
print("File closed automatically:", f.closed)

# ============================================================
# --- Quick Summary ---
# ============================================================
"""
Quick Summary:
--------------
✔ open(filename, mode) → Opens file in text or binary mode.
   Modes: 'r' (read), 'w' (write), 'a' (append), 'r+' (read/write)
✔ read() → Reads entire file as one string.
✔ readline() → Reads next line from file.
✔ readlines() → Reads all lines as a list.
✔ seek(offset) → Moves file cursor to position.
✔ tell() → Returns current cursor position.
✔ close() → Closes file manually.
✔ with open() → Automatically handles open and close (best practice).
"""
