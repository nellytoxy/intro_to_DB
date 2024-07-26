import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="May251993@@##"
)

mycursor = mydb.cursor()


try:
        mycursor.execute ("""CREATE DATABASE IF NOT EXISTS alx_book_store 

        """)
        print("Database 'alx_book_store created successfully")
except Exception as mysql_connector_Error:
        print("except Exception as mysql_connector_Error")

mycursor.close()
mydb.close()


mycursor.close()
mydb.close()

