import requests
import mysql.connector
from bs4 import BeautifulSoup

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="teachinginvietnam"
)
source = requests.get('https://jobs.teachinginvietnam.org/jobs-search-page/')
soup = BeautifulSoup(source.text,'html.parser')
data_DatePosted = soup.find_all('li', class_="cs-radio-btn")
Descriptions = [] 

for i in data_DatePosted:
    dt = i.find('a').text.strip()
    Descriptions.append(dt)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE tbl_dateposted (ID INT AUTO_INCREMENT PRIMARY KEY, Description VARCHAR(255))")
sql = "INSERT INTO tbl_dateposted (ID, Description) VALUES (%s, %s)"
for a in Descriptions:
    val = ("null", a)
    mycursor.execute(sql, val)
mydb.commit()