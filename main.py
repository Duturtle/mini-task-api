from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Mini Task API", version="1.0.0")


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


class Task(TaskCreate):
    id: int


tasks: list[Task] = []
next_id = 1


@app.get("/")
def root():
    return {"message": "Mini Task API is running"}


@app.get("/tasks", response_model=list[Task])
def get_tasks():
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task_data: TaskCreate):
    global next_id

    task = Task(id=next_id, **task_data.model_dump())
    tasks.append(task)
    next_id += 1
    return task


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskCreate):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            updated_task = Task(id=task_id, **task_data.model_dump())
            tasks[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")
