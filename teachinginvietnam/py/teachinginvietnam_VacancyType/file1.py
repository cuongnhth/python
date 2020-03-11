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
data_VancancyType = soup.find('ul', class_="cs_vacancy_type")
data_VancancyTypes = data_VancancyType.find_all('li')
Descriptions = [] 

for i in data_VancancyTypes:
    dt = i.find('a').text
    Descriptions.append(dt)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE tbl_VancancyType (ID INT AUTO_INCREMENT PRIMARY KEY, Description VARCHAR(255))")
sql = "INSERT INTO tbl_VancancyType (ID, Description) VALUES (%s, %s)"
for a in Descriptions:
    val = ("null", a)
    mycursor.execute(sql, val)
mydb.commit()