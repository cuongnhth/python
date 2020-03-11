import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="academicpositions"
)
a = []
b = ["c", "a", "a", "c", "b", 1, 2, 1, 3]
for i in b:
    a.append(i)
mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE abc (ID INT AUTO_INCREMENT PRIMARY KEY, University VARCHAR(255))")
sql = "INSERT INTO abc (ID, University) VALUES (%s, %s)"

for i in a:
	val = ("null", i)
	mycursor.execute(sql, val) 
mydb.commit()
print(a)