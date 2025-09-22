# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 06:22:03 2025

@author: hamid

Program Description:
----------------------------------------------------------------------------------
This Python program registers users by taking an email and password as input.
    The email must follow the format expression@string.string (e.g., user123@gmail.com).
    The password must contain both letters and numbers.
    After validation, the information is stored in a MySQL database (user_database, table users).
    Finally, the program displays all registered users.
"""
import re
import mysql.connector
from mysql.connector import Error

def is_valid_email(email):
    #Check if email matches expression@string.string

    pattern = r'^[A-Za-z0-9]+@[A-Za-z]+\.[A-Za-z]+$'
    return re.match(pattern, email) is not None

def is_valid_password(password):
    #Password must contain at least one letter and one digit
    
    has_letter = any(c.isalpha() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_letter and has_digit

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
        cursor.execute("CREATE DATABASE IF NOT EXISTS user_database")
        print("✅ Database 'user_database' created successfully!")

        # Switch to user_database
        cursor.execute("USE user_database")

        # Create a table with username (email) and password
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(100) NOT NULL,
                password VARCHAR(100) NOT NULL
            )
        """)
        print("✅ Table 'users' created successfully!")

        # Confirm current DB
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("📂 You are connected to database:", record[0])

        # Get email input with validation
        while True:
            email = input("Enter your email: ").strip()
            if is_valid_email(email):
                break
            else:
                print("❌ Invalid email format! Example: example123@gmail.com")

        # Get password input with validation
        while True:
            password = input("Enter your password: ").strip()
            if is_valid_password(password):
                break
            else:
                print("❌ Password must contain both letters and numbers.")

        # Insert into DB
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (email, password)
        )
        connection.commit()
        print("✅ User registered successfully!")

        # Fetch all users
        cursor.execute("SELECT username, password FROM users;")
        rows = cursor.fetchall()

        print("\n📊 Registered Users:")
        for username, password in rows:
            print(f"{username} | {password}")

except Error as e:
    print("❌ Error while connecting to MySQL:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("🔌 MySQL connection closed")
