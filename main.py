from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import mysql.connector


app = FastAPI()


app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


db = mysql.connector.connect(

    host="localhost",
    user="root",
    password="durai123",
    database="new_one"
)

cursor = db.cursor()



class Student(BaseModel):

    name: str
    email: str



@app.get("/")

def home():

    return {

        "message":
        "AI Education App Running Successfully"
    }



@app.post("/register")

def register(student: Student):

    sql = """

    INSERT INTO student_details(name, email)

    VALUES(%s, %s)

    """

    values = (

        student.name,
        student.email
    )

    cursor.execute(sql, values)

    db.commit()

    return {

        "message":
        "Student Registered Successfully"
    }



@app.get("/students")

def get_students():

    cursor.execute(

        "SELECT * FROM student_details"
    )

    data = cursor.fetchall()

    students = []


    for row in data:

        students.append({

            "id": row[0],
            "name": row[1],
            "email": row[2]
        })

    return students



@app.get("/chatbot")

def chatbot(q: str):

    question = q.lower()


    if "python" in question:

        answer = (
            "Python is a programming language"
        )

    elif "ai" in question:

        answer = (
            "AI means Artificial Intelligence"
        )

    else:

        answer = (
            "Please ask education related questions"
        )


    return {

        "question": q,
        "response": answer
    }



@app.get("/quiz")

def quiz():

    questions = [

        {
            "question":
            "What is Python?",

            "answer":
            "Programming Language"
        },

        {
            "question":
            "What is AI?",

            "answer":
            "Artificial Intelligence"
        },

        {
            "question":
            "What is Machine Learning?",

            "answer":
            "Subset of AI"
        }
    ]

    return questions