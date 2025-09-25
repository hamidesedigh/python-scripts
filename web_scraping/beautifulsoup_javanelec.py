# -*- coding: utf-8 -*-
"""
Created on Fri Jul  4 21:24:40 2025

@author: hamid
"""

import requests
import bs4


r = requests.get("https://www.javanelec.com/")

if r.status_code == 200:
    data = r.text
    soup = bs4.BeautifulSoup(data, "html.parser")
    t = soup.select("title")
    mytitle = t[0]
    titr = mytitle.get_text()
else:
    print("The page is not found")



print(f" Title of this website is:\n {titr.center(60)}")

products = soup.find_all(class_='prd-main-cat')

print("List of products are:")
for product in products:
    # a new line
    for line in product.stripped_strings:
        print(line)


print("List of pictures are here:")
# Find all img tags
images = soup.find_all('img')

# Loop through all images and get their src attribute
for idx, img in enumerate(images):
    src = img.get('src')
    # Build full URL
    full_url = 'https://www.javanelec.com' + src if src.startswith('/') else src
    print(f"Image {idx+1}: {full_url}")
