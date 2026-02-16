from fastapi import FastAPI
from student import Student

app = FastAPI()

list = [Student(id=1, name="Brajesh", age=25, email="brajesh@example.com")
        ,Student(id=2, name="Rajesh", age=35, email="rajesh@example.com"),
        Student(id=3, name="Akshay", age=30, email="akshay@example.com"),
        Student(id=4, name="Hemant", age=12, email="hemant@example.com")]

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

@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in list:
        if student.id == student_id:
            return student
    return {"message": "Student not found"}
