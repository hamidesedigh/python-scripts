# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 06:22:42 2025

Sample Input:
The Persian League is the largest sport event dedicated to the deprived areas of Iran. 
The Persian League promotes peace and friendship. 
This video was captured by one of our heroes who wishes peace.

Sample Output:
    
2:Persian
3:League
15:Iran
17:Persian
18:League

@author: hamid
"""

def word_index(text):
    words = text.split()
    keywords = []
    index = 1
    sentence_start = True
    
    for word in words:
        # Omit '.,'
        clean_word = word.strip('.,')
        
        # Check on the the second word of the sentence
        if sentence_start:
            sentence_start = False
        else:
            if clean_word and clean_word[0].isupper() and not clean_word.isdigit():
                keywords.append(f"{index}:{clean_word}")
        
        # Check end of the sentence
        if word.endswith('.'):
            sentence_start = True
        
        # Increasing the index
        index += 1
    
    if keywords:
        for k in keywords:
            print(k)
    else:
        print("None")


def main():
    text = input().strip()
    word_index(text)
    
    
    
if __name__ == "__main__":
    main()