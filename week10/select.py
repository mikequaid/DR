import mysql.connector
import dbconfig as config

db = mysql.connector.connect(
  host=config.mysql['host'],
  user=config.mysql['username'],
  password=config.mysql['password'],
  database=config.mysql['database']
)

cursor = db.cursor()
sql="select * from student"


cursor.execute(sql)
result = cursor.fetchall()
for x in result:
  print(x)