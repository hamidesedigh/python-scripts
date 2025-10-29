# -*- coding: utf-8 -*-
"""
main.py – demo runner for mylibrary
"""

from mylibrary.library import Library


def menu() -> None:
    print("\n" + "*" * 45)
    print("📚 Welcome to the University Library 📚")
    print("*" * 45)
    print("""
Available commands:
  ➕ add     → add a new book
  ❌ remove  → remove a book
  🔍 search  → search for a book
  📖 show    → list all books
  🚪 exit    → exit the program
""")


def main() -> None:
    lib = Library()
    menu()
    while True:
        cmd = input("\nEnter command: ").strip().lower()

        if cmd == "add":
            title = input("Book title: ")
            author = input("Author: ")
            lib.add_book(title, author)
        elif cmd == "remove":
            title = input("Book title to remove: ")
            lib.remove_book(title)
        elif cmd == "search":
            title = input("Book title to search: ")
            lib.search_book(title)
        elif cmd == "show":
            lib.show_books()
        elif cmd == "exit":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Unknown command. Please try again.")


if __name__ == "__main__":
    main()
