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
data_Gender = soup.find('form', id="frm_gender").find('ul', class_="custom-listing")
data_Genders = data_Gender.find_all('a')
Descriptions = [] 

for i in data_Genders:
  dt = i.text.strip()
  Descriptions.append(dt)

# for a in Descriptions:
#   print(a)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE tbl_Gender (ID INT AUTO_INCREMENT PRIMARY KEY, Description VARCHAR(255))")
sql = "INSERT INTO tbl_Gender (ID, Description) VALUES (%s, %s)"
for a in Descriptions:
    val = ("null", a)
    mycursor.execute(sql, val)
mydb.commit()