# -*- coding: utf-8 -*-
"""
mylibrary.library
-----------------
Core module defining the Library class.
"""

from typing import List


class Library:
    """A simple in-memory library manager."""

    def __init__(self) -> None:
        self.books: List[str] = []
        self.authors: List[str] = []

    def add_book(self, title: str, author: str) -> None:
        """Add a book to the library."""
        if title in self.books:
            print(f"⚠️ '{title}' already exists.")
            return
        self.books.append(title)
        self.authors.append(author)
        print(f"✅ Added '{title}' by {author}")

    def remove_book(self, title: str) -> None:
        """Remove a book by title."""
        if title not in self.books:
            print(f"❌ '{title}' not found.")
            return
        idx = self.books.index(title)
        self.books.pop(idx)
        self.authors.pop(idx)
        print(f"🗑️ Removed '{title}'")

    def search_book(self, title: str) -> bool:
        """Return True if book exists, else False."""
        found = title in self.books
        print(f"🔍 '{title}' {'found' if found else 'not found'}")
        return found

    def show_books(self) -> None:
        """Display all stored books."""
        if not self.books:
            print("📚 No books in library yet.")
            return
        for t, a in zip(self.books, self.authors):
            print(f"• {t} — {a}")

    def __len__(self) -> int:
        return len(self.books)
