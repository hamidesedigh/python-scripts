# -*- coding: utf-8 -*-
"""
Created on Fri Jul  4 21:24:40 2025
@author: Hamideh

Program Description:
--------------------
This program performs web scraping on the official website of Javan Elec (https://www.javanelec.com/)
using the `requests` and `BeautifulSoup` libraries.

Main Features:
1. Connects to the website and retrieves its HTML content.
2. Extracts and displays the title of the webpage.
3. Finds and lists all available product categories shown on the homepage.
4. Extracts and prints all image URLs found in the HTML source.
5. Saves both the product list and image URLs into a CSV file for further analysis.

The program checks for a successful HTTP response (status code 200) before parsing the HTML.
If the page is not found, it displays an appropriate message.

Output:
-------
- The title of the website.
- A list of product categories.
- A list of image URLs found on the page.
- A CSV file named `javanelec_data.csv` containing both lists.
"""

import requests
import bs4
import csv

# Step 1: Send request
r = requests.get("https://www.javanelec.com/")

if r.status_code == 200:
    data = r.text
    soup = bs4.BeautifulSoup(data, "html.parser")

    # Step 2: Extract the title
    title_tag = soup.select_one("title")
    titr = title_tag.get_text() if title_tag else "No title found"
    print(f"\n Title of this website is:\n {titr.center(60)}\n")

    # Step 3: Extract product categories
    products = []
    product_sections = soup.find_all(class_='prd-main-cat')

    print("List of products are:")
    for product in product_sections:
        for line in product.stripped_strings:
            products.append(line)
            print(line)

    # Step 4: Extract all images
    images = []
    print("\nList of pictures are here:")
    image_tags = soup.find_all('img')

    for idx, img in enumerate(image_tags):
        src = img.get('src')
        if src:
            full_url = 'https://www.javanelec.com' + src if src.startswith('/') else src
            images.append(full_url)
            print(f"Image {idx+1}: {full_url}")

    # Step 5: Save data to CSV file
    filename = "javanelec_data.csv"
    with open(filename, mode="w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Image_URL"])
        max_len = max(len(products), len(images))
        for i in range(max_len):
            cat = products[i] if i < len(products) else ""
            img = images[i] if i < len(images) else ""
            writer.writerow([cat, img])

    print(f"\n✅ Data has been successfully saved to '{filename}'.")

else:
    print("❌ The page is not found.")
