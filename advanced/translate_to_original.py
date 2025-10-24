# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 07:11:20 2025
@author: Hamideh

Description:
------------
This program translates a sentence back to its original words using a dictionary
mapping of translations in English, French, and German to the original word.

Steps:
1. Reads the number of dictionary entries.
2. For each entry, reads the original word and its translations in English, French, and German.
3. Builds a dictionary that maps any translation to the original word.
4. Reads a sentence and replaces each word with its original word if it exists in the dictionary.
5. Prints the translated sentence, leaving words unchanged if no translation is found.

Example Input:
--------------
3
chat cat chat Katze
chien dog chien Hund
maison house maison Haus
I have a dog and a cat

Example Output:
---------------
I have a chien and a chat
"""


def main():
    """Main function: builds dictionary and translates the input sentence."""

    # Read number of dictionary entries
    number_of_words = int(input().strip())

    # Build a translator dictionary mapping any translation → original word
    translator = {}
    for _ in range(number_of_words):
        original, english, french, german = input().strip().split()
        translator[english] = original
        translator[french] = original
        translator[german] = original

    # Read the sentence to be translated
    text = input().strip()
    words = text.split()

    # Translate each word if present in dictionary, else keep it unchanged
    result = [translator.get(word, word) for word in words]

    # Print the translated sentence
    print(" ".join(result))


if __name__ == "__main__":
    main()
