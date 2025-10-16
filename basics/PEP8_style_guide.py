# -*- coding: utf-8 -*-
"""
@author: hamid
Created on Wed Sep 27 14:15:32 2025

This module demonstrates PEP 8 style guide conventions
for parameters, variables, functions, and file definitions.
https://peps.python.org/pep-0008/

🔑 PEP 8 Highlights in This Example

File name: all lowercase with underscores (example_module.py).
Imports: at the top, grouped, one per line.
Constants: ALL_CAPS with underscores (PI_APPROX, DEFAULT_RADIUS).
Functions: snake_case (calculate_area, print_circle_info, main).
Parameters & variables: snake_case (radius, circle_area, user_radius).
Docstrings: triple quotes, short description, then detailed sections.
Indentation & spacing: 4 spaces per indent, spaces around operators, blank lines to separate functions.
Entry point: if __name__ == "__main__": at the bottom.

"""
# Standard library imports (grouped and sorted alphabetically)
import math
import os


# Global constants are written in ALL_CAPS with underscores
PI_APPROX = math.pi
DEFAULT_RADIUS = 5


def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    Parameters
    ----------
    radius : float
        The radius of the circle.

    Returns
    -------
    float
        The area of the circle.
    """
    # Local variable in snake_case
    area = PI_APPROX * radius ** 2
    return area


def print_circle_info(radius: float = DEFAULT_RADIUS) -> None:
    """
    Print the radius and area of a circle.

    Parameters
    ----------
    radius : float, optional
        The radius of the circle (default is DEFAULT_RADIUS).
    """
    circle_area = calculate_area(radius)
    print(f"Radius: {radius}, Area: {circle_area:.2f}")


def main() -> None:
    """
    Main entry point of the program.
    """
    # Variables in snake_case
    user_radius = 7.5
    print_circle_info(user_radius)
    print_circle_info()  # Uses default parameter


# Standard Python entry point
if __name__ == "__main__":
    main()