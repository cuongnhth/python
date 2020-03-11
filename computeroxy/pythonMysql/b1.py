import requests
import datetime
import mysql.connector
from bs4 import BeautifulSoup
import re

source = requests.get('https://computeroxy.com/announcements,a.html')
soup = BeautifulSoup(source.text, 'html.parser')
accListPresent = soup.find_all('div', class_='accItemPresent')

Title = []	
University = []		
Country = []
Link = []
Email = []
Time = []
row = []
table = []
for i in accListPresent:
	mark = i.find('div', class_='mark')
	if mark:
		if "PRIORITY!" in mark.text:
			h3 = i.find('h3')
			Title = h3.find("a").text.strip()
			row.append(Title)

			smalls = h3.find_all('small')
			University = (smalls[0].text)
			row.append(University)

			Country = (smalls[1].text)
			row.append(Country)

			links = h3.find('a').get('href')
			if(re.search("https", links) != None):
				row.append(links)
			else:
				row.append("https://computeroxy.com"+links)

			scrape = requests.get(row[3])
			scrape = BeautifulSoup(scrape.text, 'html.parser')
			scrape = scrape.get_text()
			emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", scrape)
			row.append(emails)
			
			x = datetime.datetime.now()
			row.append(x)

			table.append(row)
			row = []

for a in table:
	print(a[0])
	print(a[1])
	print(a[2])
	print(a[3])
	print(a[4])
	print(a[5])
	print("------------------------")
