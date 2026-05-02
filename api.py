from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import os

app = FastAPI()

# ✅ CORS (important)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

FILE_NAME = "tasks.json"

# Load tasks
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

tasks = load_tasks()

class Task(BaseModel):
    title: str

# ➤ Add Task
@app.post("/add")
def add_task(task: Task):
    priority = "High" if "urgent" in task.title.lower() else "Normal"

    new_task = {
        "task": task.title,
        "priority": priority
    }

    tasks.append(new_task)
    save_tasks(tasks)

    return {"message": "Task added", "task": new_task}

# ➤ Get Tasks
@app.get("/tasks")
def get_tasks():
    return tasks

# ➤ Suggest Task
@app.get("/suggest")
def suggest_task():
    if not tasks:
        return {"suggestion": "No tasks available"}

    for t in tasks:
        if t["priority"] == "High":
            return {"suggestion": f"Do this first: {t['task']}"}

    return {"suggestion": f"Start with: {tasks[0]['task']}"}

# ➤ Count Tasks
@app.get("/count")
def count_tasks():
    return {"total": len(tasks)}

# ➤ Delete Task
@app.delete("/delete/{index}")
def delete_task(index: int):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        return {"message": "Task deleted", "task": removed}
    
    return {"error": "Invalid index"}