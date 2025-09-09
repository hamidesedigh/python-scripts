# -*- coding: utf-8 -*-
"""
Created on Tue Sep  9 06:04:46 2025
Read the final list of computer Olympiad finalists and prepare entry cards for the results committee.
The input records include gender, name, and the language used, with a non-standard registration format.
Standardize the names, group by gender, and attach the corresponding language to each name.

@author: hamid
"""

def main():
    
    # Enter the number of people
    cnt = int(input().strip())
    people_list = []
    
    for _ in range(cnt):
        data = input().strip().split('.')
        data[1] = data[1].capitalize()
        people_list.append(data)        
    
    # Sorting 
    sorted_list = sorted(people_list, key = lambda x: (x[0], x[1]))

    # print
    for g in sorted_list:
        print(f"{g[0]} {g[1]} {g[2]}")
        
        
if __name__ == "__main__":
    main()
