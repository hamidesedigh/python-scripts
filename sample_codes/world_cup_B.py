# -*- coding: utf-8 -*-
"""
Created on Sun Aug 31 06:41:56 2025

In Group B of the FIFA World Cup, the teams Iran, Portugal, Spain, and Morocco participate.
Write a program that, given the match results, prints for each team the name, number of wins, losses, goal difference,
and points, in order of points on a single line per team. Each team's line should be printed in that order.
If points are tied, compare the number of wins; if both wins and points are equal, sort alphabetically.

Notes:
- A win gives 3 points, a draw 1 point, and a loss 0 points.
- Goal difference is the difference between goals scored and goals conceded for a team.

The match results should be read in the following order
(in the input example, the number on the left corresponds to the team on the right):
Iran – Spain
Iran – Portugal
Iran – Morocco
Spain – Portugal
Spain – Morocco
Portugal – Morocco

Sample Input:
2-2
2-1
1-2
2-2
3-1
2-1

Sample Output:
Spain wins:1 , loses:0 , draws:2 , goal difference:2 , points:5
Iran wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Portugal wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
Morocco wins:1 , loses:2 , draws:0 , goal difference:-2 , points:3

@author: hamide
"""
from itertools import combinations

class Team:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.loses = 0
        self.draws = 0
        self.goal = 0
        self.goal_ = 0
        self.goal_diff = 0
        self.points = 0

    def update_team_goal(self, goal, goal_):
        if goal > goal_:
            self.wins += 1
        elif goal < goal_:
            self.loses += 1
        else:
            self.draws += 1

        self.goal += goal
        self.goal_ += goal_

    def update_team_result(self):
        self.goal_diff = self.goal - self.goal_
        self.points = 3 * self.wins + self.draws


def main():
    # Teams
    Iran = Team('Iran')
    Spain = Team('Spain')
    Portugal = Team('Portugal')
    Morocco = Team('Morocco')
    teams = {'Iran': Iran, 'Spain': Spain, 'Portugal': Portugal, 'Morocco': Morocco}

    # Generate all match pairs
    for first, second in combinations(teams.keys(), 2):
        val = input().strip()
        a, b = map(int, val.split("-"))

        # update both teams correctly
        teams[first].update_team_goal(a, b)
        teams[second].update_team_goal(b, a)

    # finalize results
    for t in teams.values():
        t.update_team_result()

    # sorting and print table
    sorted_teams = sorted(
        teams.items(),
        key = lambda item: (-item[1].points, -item[1].wins, item[0])
    )

    for name, t in sorted_teams:
        print(
            f"{name}  wins:{t.wins} , loses:{t.loses} , draws:{t.draws}, goal difference:{t.goal_diff} , points:{t.points} ")


if __name__ == "__main__":
    main()