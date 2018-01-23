-*- coding: utf-9 -*-

#importing libraries
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime

#url we need
quote_page = 'http://www.bloomberg.com/quote/SPX:IND'

#getting the webpage and parse using beautiful soup
page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')

#Taking out <div> and getting its value
name_container = soup.find('h1', attrs={'class': 'name'})
name = name_container.text.strip()

#getting price
price_container = soup.find('div', attrs={'class': 'price'})
price = price_container.text

# open a csv file with append, so old data will not be erased
with open(‘index.csv’, ‘a’) as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow([name, price, datetime.now()])


