import mysql.connector

mydb = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password ='',
	database = 'e-ViVa',
)

if mydb.is_connected():
	print("Succesfully Connected")