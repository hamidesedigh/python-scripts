# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 06:13:06 2025
@author: Hamideh

Program Description:
--------------------
This script creates a list of football players, randomly assigns them
to two teams (A and B), and prints out the final team assignments.

Features:
---------
- Defines a base class `Person`.
- Defines a derived class `FootballPlayer` that can be assigned to a team.
- Randomly divides players into two approximately equal teams.
- Prints each player's name alongside their assigned team.
"""

import random


class Person:
    """Base class representing a person with a name."""

    def __init__(self, name: str):
        self.name = name


class FootballPlayer(Person):
    """Represents a football player who belongs to a team."""

    def set_team(self, team: str) -> None:
        """Assign the player to a team."""
        self.team = team

    def __str__(self) -> str:
        """Return string representation of the player and their team."""
        return f"{self.name} - {self.team}"


def assign_players_to_teams(players, teams):
    """
    Randomly assign players to the given teams.

    Parameters:
        players (list): A list of FootballPlayer objects.
        teams (list): A list of team names (e.g., ["A", "B"]).
    """
    num_players = len(players)
    half = num_players // len(teams)

    indices = list(range(num_players))
    random.shuffle(indices)

    # Split indices into roughly equal groups
    split_indices = [indices[i * half:(i + 1) * half] for i in range(len(teams) - 1)]
    split_indices.append(indices[(len(teams) - 1) * half:])  # Include any remaining players

    # Assign players to teams
    for team_name, team_indices in zip(teams, split_indices):
        for idx in team_indices:
            players[idx].set_team(team_name)


def main():
    """Main function to create players, assign teams, and display results."""
    names = [
        "حسین", "مازیار", "اکبر", "نیما", "مهدی", "فرهاد", "محمد", "خشایار", "میلاد", "مصطفی",
        "امین", "سعید", "پویا", "پوریا", "رضا", "علی", "بهزاد", "سهیل", "بهروز", "شهروز",
        "سامان", "محسن"
    ]

    players = [FootballPlayer(name) for name in names]
    teams = ["A", "B"]

    assign_players_to_teams(players, teams)

    print("Team Assignments:")
    print("-" * 20)
    for player in players:
        print(player)


if __name__ == "__main__":
    main()
