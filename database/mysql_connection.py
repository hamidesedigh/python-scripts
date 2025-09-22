# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 21:50:29 2025

@author: hamid

Program Description:
--------------------
Connect to MySQL database using mysql.connector

Installing the Connector
------------------------
pip install mysql-connector-python
pip list

Creating a db by MYSQL 8.0 Command Line Client
----------------------------------------------
CREATE DATABASE mydb;
USE mydatabase;
SELECT DATABASE();   # Check which database you’re using
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

SHOW TABLES;
DESC users;
INSERT INTO users (name, email)
VALUES ('Alice2', 'alice@example.com'),
       ('Bob2', 'bob@example.com');

SELECT * FROM users;


"""

import mysql.connector
from mysql.connector import Error

try:
    # Establish connection
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="9543",
        database="mydb"
    )

    if connection.is_connected():
        print("✅ Successfully connected to MySQL")

        cursor = connection.cursor()

        # Confirm current DB
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("📂 You are connected to database:", record[0])

        # Insert new data
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s)",
            ("Hamideh", "hamidesedigh@gmail.com")
        )
        connection.commit()
        print("✅ Data inserted successfully!")

        # Fetch all rows from users
        cursor.execute("SELECT * FROM users;")
        rows = cursor.fetchall()

        print("\n📊 Users table content:")
        for row in rows:
            print(row)
        
        # Delete new inserted data
        cursor.execute(
            "DELETE FROM users WHERE name = %s LIMIT 3",
            ("Hamideh",))
        connection.commit()
        print("🗑️ User deleted successfully!")
        
        # Fetch and print all data after deletion
        cursor.execute("SELECT id, name, email FROM users;")
        rows = cursor.fetchall()
        
        print("\n📊 Users table content after deletion:")
        for (id, name, email) in rows:
            print("%d. %s is %s in the mydb" % (id, name, email))

except Error as e:
    print("❌ Error while connecting to MySQL:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("\n🔌 MySQL connection closed")
