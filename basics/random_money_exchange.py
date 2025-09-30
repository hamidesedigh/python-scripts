# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 23:38:43 2025

@author: hamid

Problem 1: random money exchange
---------------------------------------------------------------------------------
This program simulates a simple model of wealth exchange
among a fixed number of people. Each person starts with
the same amount of money. In each round, every person who
has at least 1 unit of money randomly selects another person
and gives them 1 unit of money (if the chosen person also
has nonzero money).
"""

import random
import matplotlib.pyplot as plt

def simulate_exchange(people_num: int = 100, initial_money: int = 100, rounds: int = 10_000) -> list[int]:
    """
    Simulate random money exchanges among people.

    Parameters:
        people_num (int): Number of people in the simulation.
        initial_money (int): Initial money each person has.
        rounds (int): Number of exchange rounds.

    Returns:
        list[int]: Final distribution of money among people.
    """
    random.seed()
    people = [initial_money] * people_num

    for _ in range(rounds):
        for person1 in range(people_num):
            if people[person1] > 0:
                person2 = random.randrange(people_num)
                if people[person2] > 0:
                    people[person1] -= 1
                    people[person2] += 1
    return people

if __name__ == "__main__":
    final_distribution = simulate_exchange()

    # Sort for visualization
    sorted_people = sorted(final_distribution)

    # Plot distribution
    plt.figure(figsize=(10, 5))
    plt.bar(range(len(sorted_people)), sorted_people, color="skyblue", edgecolor="black")
    plt.xlabel("Individuals (sorted by wealth)")
    plt.ylabel("Money")
    plt.title("Wealth Distribution after Random Exchanges")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
