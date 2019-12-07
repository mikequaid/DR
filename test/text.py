#import mysql.connector

#db = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  password="root"
#)

#cursor = db.cursor()

#cursor.execute("CREATE DATABASE datarepresentation")

import pandas as pd
import world_bank_data as wb
pd.set_option('display.max_rows', 6)