# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 06:13:06 2025

@author: hamid

Program Description:
--------------------
This script creates a list of football players, randomly assigns them 
to two teams (A and B), and prints the team assignments.

"""

import random
import numpy as np

class Person:
    # Base class representing a person with a name.
    def __init__(self, name):
        self.name = name
        

class FootballPlayer(Person):
    # Represents a football player who belongs to a team.
    def set_team(self, team):
        # Assign the player to a team.
        self.team = team
        
    def __str__(self):
        return f"{self.name} - {self.team}"


def assign_players_to_teams(players, teams):
    # Randomly assign players to teams.
    # Assumes number of players can be divided roughly evenly.
    
    half = len(names) // 2
    indices = list(range(len(names)))
    random.shuffle(indices)
    
    A_idx = indices[:half]
    B_idx = indices[half:]
    
    
    for idx in A_idx:
        players[idx].set_team("A")
        
    for idx in B_idx:
        players[idx].set_team("B")


# ===========================
# Main Program
# ===========================

names = ["حسین","مازیار","اکبر","نیما","مهدی","فرهاد","محمد","خشایار","میلاد","مصطفی", "امین","سعید","پویا","پوریا","رضا","علی","بهزاد","سهیل","بهروز","شهروز","سامان","محسن"]

players = [FootballPlayer(name) for name in names]

teams = ["A", "B"]

assign_players_to_teams(players, teams)

for p in players:
    print(p)


