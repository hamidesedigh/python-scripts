# -*- coding: utf-8 -*-
"""
matplotlib_plot.py
-----------------------------------------------------------
Demonstrates simple data visualization using Matplotlib.
"""

import matplotlib.pyplot as plt
import numpy as np

def main():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label="sin(x)", color="blue")
    plt.title("Sine Function")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
