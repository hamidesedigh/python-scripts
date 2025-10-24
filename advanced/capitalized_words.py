# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 06:22:42 2025
@author: Hamideh

Description:
------------
This program identifies words in a text that are capitalized and **not the first word of a sentence**.
It ignores numbers and punctuation marks like '.' and ','.

For each such word, it prints its position in the text (starting from 1) along with the word.

Example Input:
--------------
The Persian League is the largest sport event dedicated to the deprived areas of Iran.
The Persian League promotes peace and friendship.
This video was captured by one of our heroes who wishes peace.

Example Output:
---------------
2:Persian
3:League
15:Iran
17:Persian
18:League
"""

def word_index(text: str) -> None:
    """
    Prints the position and value of capitalized words in the text
    that are not the first word of a sentence.
    """
    words = text.split()
    keywords = []
    index = 1
    sentence_start = True  # Flag to detect the first word of a sentence

    for word in words:
        # Remove punctuation from word
        clean_word = word.strip('.,')

        # Only consider capitalized words not at the start of a sentence
        if sentence_start:
            sentence_start = False
        else:
            if clean_word and clean_word[0].isupper() and not clean_word.isdigit():
                keywords.append(f"{index}:{clean_word}")

        # Reset flag at the end of a sentence
        if word.endswith('.'):
            sentence_start = True

        index += 1

    # Print results
    if keywords:
        for k in keywords:
            print(k)
    else:
        print("None")


def main():
    """Read input text and process capitalized words."""
    text = input().strip()
    word_index(text)


if __name__ == "__main__":
    main()
