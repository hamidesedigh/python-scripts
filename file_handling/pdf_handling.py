# -*- coding: utf-8 -*-
"""
@author: Hamideh
Created on Wed Oct  8 12:13:43 2025

Program Description:
-------------------------
Demonstration of PDF File Creation and Reading
--------------------------------------------------------------
Covers:
✔ reportlab for PDF creation
✔ PyPDF2 for reading and merging
✔ Writing text and reading metadata
"""

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import PyPDF2

# --- Create PDF ---
pdf_file = "sample.pdf"
c = canvas.Canvas(pdf_file, pagesize=A4)
c.drawString(100, 800, "Hello, everyone! I am Hamideh! This is a PDF demo to use Python on PDF files.")
c.drawString(100, 780, "Created using reportlab.")
c.save()
print("✅ PDF file created.")

# --- Read PDF ---
with open(pdf_file, "rb") as f:
    reader = PyPDF2.PdfReader(f)
    print("\nNumber of Pages:", len(reader.pages))
    first_page = reader.pages[0]
    print("Page Text:", first_page.extract_text())

"""
Quick Summary:
--------------
✔ reportlab → Create PDF files programmatically
✔ PyPDF2 → Read, split, merge, or extract PDF content
"""
