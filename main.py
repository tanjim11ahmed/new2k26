from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome Tanjim!"}


@app.get("/student")
def get_students():
    return {"message": "All Students"}


@app.get("/student/{id}")
def get_student(id: int):
    return {"student_id": id}


@app.get("/teacher")
def teacher():
    return {"name": "Tanjim MSc"}


@app.get("/teacher/{id}")
def teacher_by_id(id: int):
    return {"teacher_id": id}


@app.get("/search")
def search(name: str):
    return {"student_name": name}


@app.get("/college")
def college():
    return {"name": "GNIBC"}


@app.get("/about")
def about():
    return {
        "developer": "Tanjim Ahmed",
        "mission": "2 Crore in 2 Years"
    }


students = []
from pydantic import BaseModel
class student(BaseModel):
    name: str
    department: str
    age: int


@app.post("/student")
def create_student(student: student):
    students.append(student)

    return {
        "Message": " Student added successfully"
    }
@app.get("/students")
def get_students():
    return students
       
@app.put("/student/{id}")
def update_student(id: int, student: student):

    if id >= len(students):
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    students[id] = student

    return {
        "message": "Student Updated Successfully"
    }
@app.delete("/student/{id}")
def delete_student(id: int):

    if id >= len(students):
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    students.pop(id)

    return {
        "message": "Student Deleted Successfully"
    }