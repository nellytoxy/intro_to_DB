import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="May251993@@##"
)

mycursor = mydb.cursor()


mycursor.execute ("""CREATE DATABASE IF NOT EXISTS alx_book_store 

""")
print("Database 'alx_book_store created successfully")
try:
     ("""MySQLServer""")

except mysql.connector.errors.ProgrammingError:
    print("Database already created")