from fastapi import FastAPI
from student import Student

app = FastAPI()

list = [Student(name="Brajesh", age=25, email="brajesh@example.com")
        ,Student(name="Rajesh", age=35, email="rajesh@example.com"),
        Student(name="Akshay", age=30, email="akshay@example.com"),
        Student(name="Hemant", age=12, email="hemant@example.com")]

@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/students")
def std():
    return list 

@app.post("/studentRegistration")
def student_registration(student: Student):
    list.append(student)
    return {"message": "Student registered successfully"}