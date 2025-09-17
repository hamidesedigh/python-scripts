# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 07:11:20 2025

You build a dictionary mapping English/French/German words → original language word (first one in each line).

Then you loop through the sentence, check if the word exists in the dictionary, and replace it.

If not found, just keep the word.

@author: hamid
"""

def main():
    
    number_of_words = int(input().strip())
    
    # dictionary: map any of the 3 translations to the original word
    translator = {}
    
    for _ in range(number_of_words):
        original, english, french, german = input().strip().split()
        translator[english] = original
        translator[french] = original
        translator[german] = original
    
    text = input().strip()
    words = text.split()
    
    result = []
    for word in words:
        if word in translator:
            result.append(translator[word])
        else:
            result.append(word)
    
    #The join() function combines elements of a list into a single string.
    print(" ".join(result))
       
    
if __name__ == "__main__":
    main()
