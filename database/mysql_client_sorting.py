# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 07:10:03 2025
@author: hamideh

Program Description
---------------------------
This Python program connects to a MySQL database and manages employee information (name, height, weight).
It creates a database (new_database1) and a table (people) if they do not already exist.
Sample employee data is inserted into the table if it is empty.
The program retrieves and displays all employees, sorted by height in descending order, and for equal heights, by weight in ascending order.
Finally, it safely closes the database connection.
"""
import mysql.connector
from mysql.connector import Error

try:
    # Connect without specifying a database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="9543"
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Create a new database
        cursor.execute("CREATE DATABASE IF NOT EXISTS new_database1")
        print("✅ Database 'new_database' created successfully!")

        # Switch to new_database
        cursor.execute("USE new_database1")

        # Create a table with Name, Weight, Height
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS people (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                height FLOAT,
                weight FLOAT
            )
        """)
        print("✅ Table 'people' created successfully!")

        # Confirm current DB
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("📂 You are connected to database:", record[0])

        # Insert sample data (only if table is empty)
        cursor.execute("SELECT COUNT(*) FROM people")
        count = cursor.fetchone()[0]
        if count == 0:
            sample_data = [
                ("Amin", 180, 75),
                ("Mahdi", 190, 90),
                ("Mohammad", 175, 75),
                ("Ahmad", 175, 60)
            ]
            cursor.executemany(
                "INSERT INTO people (name, height, weight) VALUES (%s, %s, %s)",
                sample_data
            )
            connection.commit()
            print("✅ Sample data inserted successfully!")

        # Fetch all rows sorted by height DESC, then weight ASC
        cursor.execute("SELECT name, height, weight FROM people ORDER BY height DESC, weight ASC;")
        rows = cursor.fetchall()

        print("\n📊 Sorted Employees (by height, then weight):")
        for name, height, weight in rows:
            print(f"{name} {height} {weight}")

except Error as e:
    print("❌ Error while connecting to MySQL:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("🔌 MySQL connection closed")
