import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password= "informix",
    database= "MyFirstDB"
)
#
mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE student MODIFY id varchar(255) primary key")
