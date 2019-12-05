import csv
import sqlite3

with sqlite3.connect("db.sqlite3") as connection:
	csvWriter = csv.writer(open("output.csv", "w"))
	c = connection.cursor()

	rows = c.fetchall()
	csvWriter.writerows(rows)
