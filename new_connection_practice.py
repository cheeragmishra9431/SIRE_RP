# Importing module
import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
	host = "localhost",
    database= 'gfg',
	user = "root",
	password = "jasmine123"
)

# Printing the connection object
# print(mydb)

# cursor = mydb.cursor()
# cursor.execute("SHOW DATABASES")
 
# for x in cursor:
#   print(x)
crsr = mydb.cursor()
 
# SQL command to create a table in the database
# sql_command = """CREATE TABLE emp (
# staff_number INTEGER PRIMARY KEY,
# fname VARCHAR(20),
# lname VARCHAR(30),
# gender CHAR(1),
# joining DATE);"""
 
# # execute the statement
# crsr.execute(sql_command)

# sql_command = """INSERT INTO emp VALUES (23, "Rishabh",\
# "Bansal", "M", "2014-03-28");"""
# crsr.execute(sql_command)

# mydb.commit()

mydb.close()