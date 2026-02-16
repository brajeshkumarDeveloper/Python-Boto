from fastapi import FastAPI
from student import Student

app = FastAPI()

list = [Student("Brajesh", 25),Student("Rajesh", 35),Student("Akshay",30),Student("Hemant",12)]

@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/students")
def std():
    return list 