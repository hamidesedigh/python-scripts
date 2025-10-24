# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 17:39:57 2025
@author: Hamideh

Program Description:
-----------------------------------------------------------------
Extract ads with 'نردبان شده' tag from Divar (Tehran - first page)
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time


driver = webdriver.Chrome()
driver.get("https://divar.ir/s/tehran")
time.sleep(5)  # wait for JS to load



soup = BeautifulSoup(driver.page_source, "html.parser")
cards = soup.find_all(class_="kt-post-card__info")

i = 0
for card in cards:
    tag = card.find(class_="kt-post-card__red-text", string="نردبان شده")
    if tag:
        title_tag = card.find("h2", class_="kt-post-card__title")
        if title_tag:
            i += 1
            print("آگهی", i,":", title_tag.get_text(strip=True))
            print("وضعیت:", tag.get_text(strip=True))
            print("-" * 50)

driver.quit()





    
   