import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password= "informix",
    database= "MyFirstDB"
)

mycursor = mydb.cursor()
try:
    mycursor.execute("create table student3 (id int, name varchar(255))")
except mysql.connector.errors.ProgrammingError:
    print("Таблиця в базі даних вже існує")
