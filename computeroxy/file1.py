import requests
import datetime
import mysql.connector
from bs4 import BeautifulSoup
import re
from datetime import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="computeroxy"
)
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
			
			x = datetime.now()
			row.append(x)

			table.append(row)
			row = []

mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE tbl_computeroxy (JobTitle VARCHAR(255), University varchar(255), Country varchar(255), Email varchar(255), Date_Time varchar(255))")
sql = "INSERT INTO tbl_computeroxy (JobTitle, University, Country, Email, Date_Time) VALUES (%s, %s, %s, %s, %s)"

for a in table:
	v1 = a[0]
	v2 = a[1]
	v3 = a[2]
	v4 = str(a[4]).strip("[]") 
	v5 = str(a[5])
	val = (v1, v2, v3, v4, v5)
	mycursor.execute(sql, val) 
	v1 = []
	v2 = []
	v3 = []
	v4 = []
	v5 = []
mydb.commit()
