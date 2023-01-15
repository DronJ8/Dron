import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password= "informix",
    database= "myfirstdb"
)
#
mycursor = mydb.cursor()
mycursor.execute("INSERT INTO  student (id, name) VALUES (12, 'Jane' )")
mycursor.execute("INSERT INTO  employee (id, name, salary) VALUES (2, 'Jane', 2000 )")
mydb.commit()