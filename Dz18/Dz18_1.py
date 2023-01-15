import mysql.connector

# Create Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password= "informix"
)

mycursor = mydb.cursor()
try:
    mycursor.execute("create database MyFirstDB")
except mysql.connector.errors.DatabaseError:
    print("Така база даних існує")
