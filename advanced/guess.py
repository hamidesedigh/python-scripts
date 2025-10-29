# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 19:48:35 2025
@author: hamid
"""

import random

def guess_number():
    secret = random.randint(1, 100)  # computer chooses a number from 1 to 100
    attempts = 0

    print("I'm thinking of a number between 1 and 100.")
    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        attempts += 1
        if guess < secret:
            print("Too low — try again.")
        elif guess > secret:
            print("Too high — try again.")
        else:
            print(f"Nice! You guessed it in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_number()
