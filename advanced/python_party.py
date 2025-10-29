# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 06:48:28 2025
@author: Hamid

🎯 Funny Python Demo:
This script shows how to make your Python programs
more interactive and fun using 3rd-party libraries!

pip install emoji tqdm termcolor pyjokes art faker

"""

# --------------------------------------------------
# 1️⃣ Emojis for cheerful output 😎
# --------------------------------------------------
"""
Conflict with django environment
import emoji
print(emoji.emojize("Python is :thumbs_up:"))
print(emoji.emojize("Coding with Python is fun :red_heart: :snake:"))
"""

# --------------------------------------------------
# 2️⃣ Progress bar with tqdm ⏳
# --------------------------------------------------
from tqdm import tqdm
from time import sleep

print("\nSimulating a long task with a progress bar...\n")
for _ in tqdm(range(100), desc="Loading", ncols=75, colour='green'):
    sleep(0.02)

# --------------------------------------------------
# 3️⃣ Colorful terminal text with termcolor 🎨
# --------------------------------------------------
from termcolor import colored

print(colored("\n🎉 Task completed successfully! 🎉", "green", attrs=["bold"]))
print(colored("Warning: Python addiction ahead! 🐍", "yellow"))

# --------------------------------------------------
# 4️⃣ Random funny jokes with pyjokes 😂
# --------------------------------------------------
import pyjokes
print("\nHere's a Python joke for you:")
print(pyjokes.get_joke(language="en", category="neutral"))

# --------------------------------------------------
# 5️⃣ ASCII art with art 🖼️
# --------------------------------------------------
from art import tprint
tprint("Python Fun!", font="block")

# --------------------------------------------------
# 6️⃣ Fake data generation with faker 🧑‍💻
# --------------------------------------------------
from faker import Faker
fake = Faker()

print("\nGenerating some fake developer data:")
for _ in range(3):
    print(f"👤 Name: {fake.name()} | 💻 Email: {fake.email()} | 🌍 City: {fake.city()}")

# --------------------------------------------------
# 7️⃣ End message
# --------------------------------------------------
print(colored("\nThanks for watching this Python fun show! 🚀", "magenta", attrs=["bold"]))
#print(emoji.emojize("Keep coding and stay awesome! :sparkles: :snake:"))
