# lab3

import requests
from bs4 import BeautifulSoup
import csv

page = requests.get("https://www.myhome.ie/residential/mayo/property-for-sale?page=2")

soup = BeautifulSoup(page.content, 'html.parser')
home_file = open('week3MyHome.csv', mode='w', newline='')
home_writer = csv.writer(home_file, delimiter='\t',quotechar='"', quoting=csv.QUOTE_MINIMAL)

listings = soup.findAll("div", class_="PropertyListingCard")

for listing in listings:
    entryList = []
    price = listing.find(class_="PropertyListingCard__Price").text
    entryList.append(price)
    address = listing.find(class_="PropertyListingCard__Address").text
    entryList.append(address)
    home_writer.writerow(entryList)

home_file.close()