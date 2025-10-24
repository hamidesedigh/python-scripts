# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 17:59:03 2025
@author: Hamideh

Program Description:
-----------------------------------------------------------------
Scrape all countries from Scrapethissite, store in MySQL,
then build a simple ML model to predict country area based on population.
"""

import requests
from bs4 import BeautifulSoup
import mysql.connector
from mysql.connector import Error
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def read_website():
    """Scrape all countries from Scrapethissite"""
    url = "https://www.scrapethissite.com/pages/simple/"
    r = requests.get(url)

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")
        countries = soup.find_all("div", class_="country")

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
                    population BIGINT,
                    area FLOAT
                )
            """)

            # Clear old data to avoid duplicates
            cursor.execute("TRUNCATE TABLE countries")

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


def load_data_from_db():
    """Load country data into a Pandas DataFrame"""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="9543",
            database="world_data"
        )

        if connection.is_connected():
            query = "SELECT name, capital, population, area FROM countries"
            df = pd.read_sql(query, connection)
            return df

    except Error as e:
        print("❌ Error while reading from MySQL:", e)
        return pd.DataFrame()

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()


def train_model(df):
    """Train a simple regression model to predict Area from Population"""
    # Drop missing values
    df = df.dropna(subset=["population", "area"])

    X = df[["population"]]
    y = df["area"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)

    print("\n📊 Model Training Complete")
    print(f"R² Score: {score:.4f}")
    print(f"Equation: Area ≈ {model.coef_[0]:.6f} * Population + {model.intercept_:.2f}")

    return model


def main():
    # Step 1: Scrape and save to database
    country_data = read_website()
    if country_data:
        save_to_database(country_data)

        # Step 2: Load data from database
        df = load_data_from_db()
        print("\n🌍 Sample Data from Database:")
        print(df.head())

        # Step 3: Train model
        model = train_model(df)

        # Step 4: Test prediction
        test_pop = 50_000_000  # example: country with 50M population
        predicted_area = model.predict(pd.DataFrame({"population": [test_pop]}))[0]
        print(f"\n🔮 Predicted Area for population {test_pop:,}: {predicted_area:,.2f} km²")


if __name__ == "__main__":
    main()
