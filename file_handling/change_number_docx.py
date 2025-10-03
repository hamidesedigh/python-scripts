# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 06:51:20 2025

Author: hamid

Description:
    This script processes a Word (.docx) document, modifying digit sequences
    in each paragraph. It replaces consecutive numbers according to a custom
    rule and saves the revised document as "Revised.docx".
"""

from docx import Document


def process_text(text: str) -> tuple[str, int]:
    """
    Process a string of text by modifying digit sequences.

    Parameters:
        text (str): The input text.

    Returns:
        tuple[str, int]: The processed text and the number of fixes made.
    """
    new_text = []
    numbers_done = 0
    fixes = 0

    for char in text:
        if char.isdigit():
            fixes += 1
            if numbers_done == 0:
                new_text.append(char)
            else:
                # Replace the last digit in the current sequence
                new_text[-numbers_done] = char
            numbers_done += 1
        else:
            new_text.append(char)
            numbers_done = 0

    return "".join(new_text), fixes


def main():
    input_file = "FinalProject.docx"
    output_file = "Revised.docx"

    doc = Document(input_file)
    total_fixes = 0

    for para in doc.paragraphs:
        new_text, fixes = process_text(para.text)
        para.text = new_text
        total_fixes += fixes

    doc.save(output_file)
    print(f"✅ Processing complete. Total fixes applied: {total_fixes}")
    print(f"💾 Revised file saved as: {output_file}")


if __name__ == "__main__":
    main()
