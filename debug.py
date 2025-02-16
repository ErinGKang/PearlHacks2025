import csv
import mysql.connector
con = mysql.connector.connect(user='root', password='Tkswhgdk3308?', database = "data")

cur = con.cursor()
cur.execute ("Select * from data")
Result = cur.fetchall()
print(Result)