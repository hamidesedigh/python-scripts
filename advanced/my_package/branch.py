# -*- coding: utf-8 -*-
"""
my_package.branch
----------------
Branch module of Hamideh’s custom Python library.

Created on Sun Jun 22 07:31:31 2025
Author: Hamideh Sedigh

Description:
    This module defines a sample constant and a demo function
    to showcase how to structure a simple Python package.
"""

# ---------------------------------------------------------------------------
# Module Constants
# ---------------------------------------------------------------------------

MY_PI = 3.141592653589793  # more accurate π value


# ---------------------------------------------------------------------------
# Core Functions
# ---------------------------------------------------------------------------

def my_funcky_print() -> None:
    """
    Print a cheerful message showing this module’s origin.
    """
    print("😎 Oh, I'm so cool — greetings from my_package.branch!\n")
    print(f"📦 You are currently inside module: {__name__}\n")


# ---------------------------------------------------------------------------
# Main Guard (for direct execution)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("⚠️ This module is part of the 'my_package' package.")
    print("👉 Please import it instead of running directly.\n")
    my_funcky_print()
