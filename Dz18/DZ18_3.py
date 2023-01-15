import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password= "informix",
    database= "MyFirstDB"
)
# f
mycursor = mydb.cursor()
try:
    mycursor.execute("create table employee5 (id int auto_increment primary key, name varchar(255), salary int(6))")
except mysql.connector.errors.ProgrammingError:
    print("Таблиця в базі даних вже існує")