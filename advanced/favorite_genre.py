# -*- coding: utf-8 -*-
"""
Created on Mon Sep 8 06:44:28 2025
@author: Hamideh

Description:
------------
This program analyzes survey data from participants who were asked to list
their three favorite movie genres from a predefined list of six options:

    - Horror
    - Romance
    - Comedy
    - History
    - Adventure
    - Action

The program performs the following steps:
1. Reads the number of participants.
2. For each participant, reads their name and three selected genres.
3. Counts how many times each genre was chosen.
4. Prints all genres with their selection counts, sorted by popularity
   (descending order). If two or more genres have the same count, they are
   displayed alphabetically. Genres not selected by anyone are still shown
   with a count of zero.

Example Input:
--------------
4
hossein Horror Romance Comedy
mohsen Horror Action Comedy
mina Adventure Action History
sajjad Romance History Action

Example Output:
---------------
Action : 3
Comedy : 2
History : 2
Horror : 2
Romance : 2
Adventure : 1
"""

def main():
    """Main function that reads input, processes data, and prints results."""

    # Define the available genres
    genres = ["Horror", "Romance", "Comedy", "History", "Adventure", "Action"]

    # Initialize a counter dictionary for all genres
    genre_count = {g: 0 for g in genres}

    # Read the number of participants
    cnt = int(input().strip())

    # Read each participant’s name and their three favorite genres
    for _ in range(cnt):
        data = input().strip().split()
        name = data[0]  # Participant’s name (not used further)
        favorite_genres = data[1:]

        # Update counts for the selected genres
        for g in favorite_genres:
            if g in genre_count:
                genre_count[g] += 1

    # Sort genres by popularity (descending) and then alphabetically
    sorted_genres = sorted(genre_count.items(), key=lambda x: (-x[1], x[0]))

    # Print the results
    for g, c in sorted_genres:
        print(f"{g} : {c}")


if __name__ == "__main__":
    main()
