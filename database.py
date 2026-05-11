import mysql.connector

db = mysql.connector.connect(

    host="localhost",
    user="root",
    password="durai123",
    database="ai_education_app"
)

print("Database Connected Successfully")