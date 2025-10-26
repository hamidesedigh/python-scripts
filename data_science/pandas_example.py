"""
pandas_example.py
-----------------
Comprehensive, example-rich pandas guide.
Based on:
- MyLearningNotes.xlsx (LoadClean sheet)
- DataCamp "Pandas Basics" Cheat Sheets
- Python for Data Science Cheat Sheet (pandas section)

Covers:
1. Pandas Data Structures
2. I/O Operations (CSV, Excel, SQL)
3. Selection & Indexing
4. Dropping
5. Sorting & Ranking
6. Retrieving Information
7. Applying Functions
8. Data Alignment & Arithmetic Operations
9. Summary Statistics
10. Asking for Help

⚙️ This script was AI-assisted, generated and refined with the help of ChatGPT to accelerate learning and documentation.
"""

import pandas as pd
import numpy as np
import sqlite3

# ===============================================================
# 1. Pandas Data Structures
# ===============================================================
print("\n=== 1. Pandas Data Structures ===")

# Series
s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])
print("Series:\n", s)

# DataFrame
data = {
    'Country': ['Belgium', 'India', 'Brazil'],
    'Capital': ['Brussels', 'New Delhi', 'Brasília'],
    'Population': [11190846, 1303171035, 207847528]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# ===============================================================
# 2. I/O Operations
# ===============================================================
print("\n=== 2. I/O Operations ===")

# CSV
df.to_csv("countries.csv", index=False)
df_csv = pd.read_csv("countries.csv")
print("CSV Read:\n", df_csv)

# Excel
df.to_excel("countries.xlsx", sheet_name="Sheet1", index=False)
df_excel = pd.read_excel("countries.xlsx", sheet_name="Sheet1")
print("\nExcel Read:\n", df_excel)

# SQL
conn = sqlite3.connect(":memory:")
df.to_sql("countries_table", conn, index=False, if_exists="replace")
df_sql = pd.read_sql_query("SELECT * FROM countries_table", conn)
print("\nSQL Read:\n", df_sql)

# ===============================================================
# 3. Selection & Indexing
# ===============================================================
print("\n=== 3. Selection & Indexing ===")

print("Select column:\n", df['Country'])
print("Select multiple columns:\n", df[['Country', 'Population']])
print("Select by position (iloc):\n", df.iloc[1])
print("Select by label (loc):\n", df.loc[2, 'Capital'])

# Boolean indexing
print("Filter rows (Population > 500M):\n", df[df['Population'] > 500_000_000])

# Setting values
df.loc[0, 'Population'] = 12000000
print("After update:\n", df)

# ===============================================================
# 4. Dropping
# ===============================================================
print("\n=== 4. Dropping ===")

df_drop_row = df.drop(index=[1])
print("After dropping row index 1:\n", df_drop_row)

df_drop_col = df.drop(columns=['Capital'])
print("After dropping column 'Capital':\n", df_drop_col)

# ===============================================================
# 5. Sorting & Ranking
# ===============================================================
print("\n=== 5. Sorting & Ranking ===")

sorted_df = df.sort_values(by='Population', ascending=False)
print("Sorted by Population (desc):\n", sorted_df)

df['Rank'] = df['Population'].rank(ascending=False)
print("Rank column added:\n", df)

# ===============================================================
# 6. Retrieving Series/DataFrame Information
# ===============================================================
print("\n=== 6. Retrieving DataFrame Info ===")

print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Index:", df.index.tolist())
print("Info:")
print(df.info())
print("Describe:\n", df.describe())

# ===============================================================
# 7. Applying Functions
# ===============================================================
print("\n=== 7. Applying Functions ===")

# Apply
df['Pop_Millions'] = df['Population'].apply(lambda x: round(x / 1_000_000, 2))
print("Apply (Population in Millions):\n", df)

# Applymap
df_num = pd.DataFrame(np.random.randn(3, 3), columns=list('ABC'))
print("\nRandom DataFrame:\n", df_num)
print("After map (abs & round):\n", df_num.map(lambda x: round(abs(x), 2)))

# ===============================================================
# 8. Data Alignment & Arithmetic Operations
# ===============================================================
print("\n=== 8. Data Alignment & Arithmetic ===")

s1 = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([7, -2, 3], index=['a', 'c', 'd'])
print("Series 1:\n", s1)
print("Series 2:\n", s2)
print("Aligned addition:\n", s1 + s2)
print("Addition with fill_value=0:\n", s1.add(s2, fill_value=0))
print("Subtraction with fill_value=2:\n", s1.sub(s2, fill_value=2))
print("Multiplication with fill_value=3:\n", s1.mul(s2, fill_value=3))
print("Division with fill_value=4:\n", s1.div(s2, fill_value=4))

# ===============================================================
# 9. Summary Statistics
# ===============================================================
print("\n=== 9. Summary Statistics ===")

print("Sum:\n", df['Population'].sum())
print("Cumulative Sum:\n", df['Population'].cumsum())
print("Min / Max:\n", df['Population'].min(), "/", df['Population'].max())
print("Mean / Median:\n", df['Population'].mean(), "/", df['Population'].median())
print("Index of Min / Max:\n", df['Population'].idxmin(), "/", df['Population'].idxmax())

# ===============================================================
# 10. Asking for Help
# ===============================================================
print("\n=== 10. Asking for Help ===")
print("Help on pd.Series.loc:\n")
help(pd.Series.loc)

print("\n✅ pandas_example.py executed successfully!")
