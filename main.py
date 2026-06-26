from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Tanjim"}

@app.get("/about")
def about():
    return {"name": "Tanjim"}

@app.get("/Tskills")
def skills():
    return {
        "skills": ["Python", "SQL", "FastAPI"]
    }
@app.get("/student/{id}")
def student(id: int):
    return {"student_id": id}

@app.get("/teacher/{id}")
def teacher(id: int):
    return{"teacher_id": id}

@app.get("/search")
def search(name: str):
    return {"student_name": name}