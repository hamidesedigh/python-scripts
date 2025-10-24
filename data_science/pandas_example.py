# -*- coding: utf-8 -*-
"""
pandas_examples.py
-----------------------------------------------------------
Illustrates Pandas DataFrame creation, filtering, and summary operations.
"""

import pandas as pd

def main():
    data = {
        "Name": ["Ali", "Sara", "Reza", "Mina"],
        "Age": [25, 30, 22, 27],
        "Score": [88, 92, 79, 85]
    }

    df = pd.DataFrame(data)
    print("\n=== DataFrame ===")
    print(df)

    # Filtering
    print("\n=== Filtered (Age > 25) ===")
    print(df[df["Age"] > 25])

    # Aggregation
    print("\n=== Summary ===")
    print(df.describe())

if __name__ == "__main__":
    main()
