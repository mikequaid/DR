import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="datarepresentation"
)

cursor = db.cursor()
sql="update student set name= %s, age=%s  where id = %s"
values = ("Mark",25, 1)

cursor.execute(sql, values)

db.commit()
print("update done")