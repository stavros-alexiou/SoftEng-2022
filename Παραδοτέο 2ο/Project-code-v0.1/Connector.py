import mysql.connector

mydb = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password ='',
	database = 'bookall',
)

if mydb.is_connected():
	print("Succesfully Connected")