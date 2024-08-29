from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students_list = {
    1:{
        "name": "john",
        "age": 17,
        "class": 2016,
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: int

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[int] = None

@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student you want to view", gt=0)):
    return students_list[student_id]

@app.get("/get-by-name/{student_id}")
def get_student(name: Optional[str] = None):
    for student_id in students_list:
        if students_list[student_id]["name"] == name:
            return students_list[student_id]
        return {"Data" : "Not Fund"}

@app.post("/create-student/{student_id}")
def create_student(student_id : int, student : Student):
    if student_id in students_list:
        return {"Error" : "Student ID exists"}
    students_list[student_id] = student 
    return students_list[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students_list:
        return {"Error": "Student does not exist"}
    
    if student.name != None:
        students_list[student_id].name = student.name
    elif student.age != None:
        students_list[student_id].age = student.age
    elif student.year != None:
        students_list[student_id].year = student.year

    return students_list[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students_list:
        return {"Error" : "Student ID not in Database"}

    del students_list[student_id]
    return {"Message" : f"Student {student_id} deleted"}