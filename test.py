from bs4 import BeautifulSoup
import requests
import re
import time
import datetime
from datetime import datetime
import mysql.connector
from selenium import webdriver

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="academicpositions"
)

University = []
Address = []
Country = []
Link = []
Date_time = []
Table = []
Row = []

Chrome_path = r"C:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(Chrome_path)  # Optional argument, if not specified will search path.

i = 1
for i in range(4):
    driver.get('https://academicpositions.com/find-jobs/all-in-all-by-all-in-all/all/' + str(i))
    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')

    result = soup.find("div", class_="search-with-filter-wrapper_right right-with-margin").find('div', class_="hits-container")
    result1 = soup.find_all("div", class_="ais-hits--item")
    for a in result1:
        txt_University = a.find("div", class_="job__head").find('a').text
        Row.append(txt_University)

        Address = a.find("div", class_="job__location").find_all('a')
        txt_Address1 = Address[0].text
        Row.append(txt_Address1)

        txt_Country = a.find("div", class_="job__location").find('a').text
        txt_Country = Address[1].text
        Row.append(txt_Country)

        txt_Link = a.find("div", class_="job__head").find('a').get('href')
        Row.append(txt_Link)

        x = datetime.now()
        Row.append(x)

        Table.append(Row)
        Row = []

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE test12 (ID INT AUTO_INCREMENT PRIMARY KEY, University VARCHAR(255), Address varchar(255), Country varchar(255), Link varchar(255), Date_Time varchar(255))")
sql = "INSERT INTO test12 (ID, University, Address, Country, Link, Date_Time) VALUES (%s, %s, %s, %s, %s, %s)"

for a in Table:
	v1 = a[0]
	v2 = a[1] + " | " + a[2]
	v3 = a[2]
	v4 = a[3]
	v5 = a[4]
	val = ("null", v1, v2, v3, v4, v5)
	mycursor.execute(sql, val) 
	v1 = []
	v2 = []
	v3 = []
	v4 = []
	v5 = []

sql = "DELETE n1 FROM test12 n1, test12 n2 WHERE n1.Link = n2.Link and n1.ID > n2.ID"
mycursor.execute(sql)
mydb.commit()

