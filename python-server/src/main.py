from fastapi import FastAPI

app = FastAPI()

tasks = []

@app.post("/task")
def add_task(task: str):
    tasks.append(task)
    return {"message": "Task added successfully"}

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}