# -*- coding: utf-8 -*-
"""
Demo Script: Using My Custom Package

Created on Sun Jun 22 07:35:44 2025
Author: Hamideh Sedigh

Description:
    This script demonstrates how to use functions and variables
    from the custom package `my_package`. It imports a fun printing
    function and a constant value for π (pi).
"""

from my_package import branch


def main():
    """Run a small demo using functions from my_library."""
    print("🎉 Welcome to Hamideh’s Library Demo! 🎉\n")

    # Call a custom function from your library
    branch.my_funcky_print()

    # Show usage of a constant
    print(f"\n🔹 The value of π from my_library is: {branch.MY_PI}")

    # Show module context info
    print(f"\n📦 This script is running in module: '{__name__}'")


# Entry point check
if __name__ == "__main__":
    main()
