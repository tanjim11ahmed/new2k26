from fastapi import FastAPI

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