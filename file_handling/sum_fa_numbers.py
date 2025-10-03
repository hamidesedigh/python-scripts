# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 09:06:20 2025

Author: hamid

Description:
    This script scans a Word (.docx) file, extracts numbers written in
    English or Persian digits (with optional decimal points), and calculates
    their total sum. It also counts how many numbers were processed.
"""

from docx import Document


# Mapping Persian digits to English digits
PERSIAN_DIGITS = str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789")


def extract_and_sum_numbers(text: str) -> tuple[float, int]:
    """
    Extract numbers from text and calculate their sum.

    Parameters:
        text (str): Input text.

    Returns:
        tuple[float, int]: (sum of numbers, count of numbers)
    """
    new_num = ""
    total = 0.0
    count = 0

    for char in text:
        if char.isdigit() or char in "۰۱۲۳۴۵۶۷۸۹":
            new_num += char.translate(PERSIAN_DIGITS)
        elif char in ".٫" and new_num:
            new_num += "."
        elif new_num and new_num != ".":
            total += float(new_num)
            count += 1
            new_num = ""

    # Handle a number if text ends with it
    if new_num and new_num != ".":
        total += float(new_num)
        count += 1

    return total, count


def main():
    input_file = "FinalProject.docx"
    doc = Document(input_file)

    grand_total = 0.0
    grand_count = 0

    for para in doc.paragraphs:
        subtotal, count = extract_and_sum_numbers(para.text)
        grand_total += subtotal
        grand_count += count

    print(f"✅ Total sum of numbers: {grand_total}")
    print(f"🔢 Total numbers found: {grand_count}")


if __name__ == "__main__":
    main()
