# Mini Task API

A small REST API built with FastAPI for learning backend development and GitHub workflows.

## Features

- Create tasks
- List tasks
- Get a task by ID
- Update tasks
- Delete tasks
- Automatic API docs

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs

## API endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/` | Health/message endpoint |
| GET | `/tasks` | List all tasks |
| GET | `/tasks/{id}` | Get one task |
| POST | `/tasks` | Create a task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

Tasks are stored in memory, so they reset when the server restarts.
