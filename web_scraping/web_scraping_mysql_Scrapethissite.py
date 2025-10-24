# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 18:52:00 2025
@author: Hamideh

Program Description:
-------------------------------------------------------------
Scrapes the first 20 countries (name, capital, population, area)
from Scrapethissite and stores them in MySQL.
"""

import requests
from bs4 import BeautifulSoup
import mysql.connector
from mysql.connector import Error


def read_website():
    """Scrape first 20 countries from Scrapethissite"""
    url = "https://www.scrapethissite.com/pages/simple/"
    r = requests.get(url)

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")
        countries = soup.find_all("div", class_="country")[:20]  # first 20 countries

        country_data = []
        for c in countries:
            name = c.find("h3", class_="country-name").get_text(strip=True)
            capital = c.find("span", class_="country-capital").get_text(strip=True)
            population = c.find("span", class_="country-population").get_text(strip=True)
            area = c.find("span", class_="country-area").get_text(strip=True)

            # Clean and convert
            population = int(population.replace(",", "")) if population else None
            area = float(area) if area else None

            country_data.append((name, capital, population, area))

        return country_data

    else:
        print("❌ The page is not found")
        return []


def save_to_database(country_data):
    """Save scraped country data into MySQL"""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="9543"
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database
            cursor.execute("CREATE DATABASE IF NOT EXISTS world_data")
            cursor.execute("USE world_data")

            # Create table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS countries (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    capital VARCHAR(100) NOT NULL,
                    population INT,
                    area FLOAT
                )
            """)

            # Insert data
            cursor.executemany("""
                INSERT INTO countries (name, capital, population, area)
                VALUES (%s, %s, %s, %s)
            """, country_data)

            connection.commit()
            print(f"✅ Inserted {cursor.rowcount} rows into 'countries' table.")

    except Error as e:
        print("❌ Error while connecting to MySQL:", e)

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("🔌 MySQL connection closed")

def print_database():
    """Fetch and print all saved countries"""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="9543",
            database="world_data"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT name, capital, population, area FROM countries")
            rows = cursor.fetchall()

            print("\n🌍 Saved Countries in Database:")
            print("-" * 60)
            for row in rows:
                print(f"Name: {row[0]}, Capital: {row[1]}, "
                      f"Population: {row[2]:,}, Area: {row[3]:,.2f} km²")
            print("-" * 60)

    except Error as e:
        print("❌ Error while fetching from MySQL:", e)

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

def main():
    country_data = read_website()
    if country_data:
        save_to_database(country_data)
        print_database()


if __name__ == "__main__":
    main()