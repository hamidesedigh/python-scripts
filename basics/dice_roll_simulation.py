# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 19:05:58 2025
@Author: hamideh

Dice Roll Simulation
-----------------------------------------------------------
This program simulates rolling a fair six-sided die multiple times
and records the frequency of each outcome. The final distribution
is visualized as a bar chart.
"""

import matplotlib.pyplot as plt
import random

def simulate_dice_rolls(trials: int = 10_000) -> list[int]:
    """Simulate rolling a six-sided die 'trials' times and return the frequency of each outcome."""
    counts = [0] * 6  # indices 0–5 correspond to dice faces 1–6
    for _ in range(trials):
        dice = random.randint(1, 6)  # roll a die
        counts[dice - 1] += 1
    return counts

if __name__ == "__main__":
    random.seed()

    trials = 10_000
    results = simulate_dice_rolls(trials)

    # Plot results
    plt.figure(figsize=(8, 5))
    plt.bar(range(1, 7), results, color="skyblue", edgecolor="black")
    plt.xlabel("Dice Face")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of {trials:,} Dice Rolls")
    plt.xticks(range(1, 7))
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
