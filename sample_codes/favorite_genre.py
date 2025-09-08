# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 06:44:28 2025

In a survey of people interested in watching movies, participants were asked to write down 3 of their favorite genres. They were given 6 genres to choose from:

Horror

Romance

Comedy

History

Adventure

Action

Write a program that:

Reads the number of participants.

Then, for each participant, reads their name and their three favorite genres.

At the end, the program should print each genre along with the number of people who selected it, sorted by popularity (descending order).

If two or more genres have the same popularity, they should be printed in alphabetical order.

If a genre is not chosen by anyone, its count should be 0 and still appear in the output.

Example Input:
4
hossein Horror Romance Comedy
mohsen Horror Action Comedy
mina Adventure Action History
sajjad Romance History Action

Example Output:
Action : 3
Comedy : 2
History : 2
Horror : 2
Romance : 2
Adventure : 1

@author: hamid
"""

def main():
    
    # Dedicated Genres
    genres = ["Horror", "Romance", "Comedy", "History", "Adventure", "Action"]
    
    # initialize the genre counter
    genre_count = {g: 0 for g in genres}
    
    # Enter the number of people
    cnt = int(input().strip())
    
    for _ in range(cnt):
        data = input().strip().split()
        name = data[0]
        
        favorite_genres = data[1:]
        for g in favorite_genres:
            if g in genre_count:
                genre_count[g] +=1
    
    # Sorting
    sorted_genres = sorted(genre_count.items(), key = lambda x: (-x[1], x[0]))

    # print
    for g, c in sorted_genres:
        print(f"{g} : {c}")

if __name__ == "__main__":
    main()