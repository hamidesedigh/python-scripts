# -*- coding: utf-8 -*-
"""
FIFA World Cup Group B Standings Calculator
===========================================

Created on Sun Aug 31 06:41:56 2025
@author: Hamideh Sedigh

Description:
------------
This program calculates and prints the standings of Group B teams (Iran, Portugal,
Spain, Morocco) in the FIFA World Cup based on match results.

Each team’s statistics include:
- Wins
- Losses
- Draws
- Goal difference
- Points

Rules:
------
- Win: 3 points
- Draw: 1 point
- Loss: 0 points
- Goal difference: goals scored minus goals conceded

Sorting Order:
--------------
1. Points (descending)
2. Wins (descending)
3. Alphabetically by team name

Input:
------
Scores of the 6 matches in the following order:
1. Iran – Spain
2. Iran – Portugal
3. Iran – Morocco
4. Spain – Portugal
5. Spain – Morocco
6. Portugal – Morocco

Format for each input line: goals_team1-goals_team2 (e.g., 2-1)

Output:
-------
Each team on a single line with the format:
Team wins:x , loses:y , draws:z , goal difference:d , points:p
"""

from itertools import combinations

class Team:
    """Class to store and update a team’s statistics."""
    def __init__(self, name: str):
        self.name = name
        self.wins = 0
        self.loses = 0
        self.draws = 0
        self.goals_for = 0
        self.goals_against = 0
        self.goal_diff = 0
        self.points = 0

    def update_team_goal(self, scored: int, conceded: int):
        """Update goals, wins, draws, and losses based on a match result."""
        if scored > conceded:
            self.wins += 1
        elif scored < conceded:
            self.loses += 1
        else:
            self.draws += 1

        self.goals_for += scored
        self.goals_against += conceded

    def finalize_result(self):
        """Calculate goal difference and total points."""
        self.goal_diff = self.goals_for - self.goals_against
        self.points = 3 * self.wins + self.draws

def main():
    # Initialize teams
    teams = {
        'Iran': Team('Iran'),
        'Spain': Team('Spain'),
        'Portugal': Team('Portugal'),
        'Morocco': Team('Morocco')
    }

    # Generate all match pairs in order
    for first, second in combinations(teams.keys(), 2):
        score = input().strip()
        goals_first, goals_second = map(int, score.split("-"))

        # Update each team's stats
        teams[first].update_team_goal(goals_first, goals_second)
        teams[second].update_team_goal(goals_second, goals_first)

    # Finalize each team's statistics
    for team in teams.values():
        team.finalize_result()

    # Sort teams by points, wins, then alphabetically
    sorted_teams = sorted(
        teams.items(),
        key=lambda item: (-item[1].points, -item[1].wins, item[0])
    )

    # Print standings
    for name, team in sorted_teams:
        print(f"{name} wins:{team.wins} , loses:{team.loses} , draws:{team.draws} , "
              f"goal difference:{team.goal_diff} , points:{team.points}")

if __name__ == "__main__":
    main()
