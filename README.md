# Smart Task Manager

A full-stack Python project with backend APIs, a simple frontend UI, and MCP integration for AI-style workflows.

---

## Features
- Add, view, and delete tasks  
- Automatic priority detection (e.g., "urgent" → High priority)  
- Smart task suggestion (AI-like logic)  
- Persistent storage using JSON  
- REST API built with FastAPI  
- Frontend using HTML and JavaScript  
- MCP server integration (tools and resources)  

---

## Tech Stack
- Python  
- FastAPI  
- HTML, JavaScript  
- JSON  
- MCP (Model Context Protocol)  

---

## Project Structure
```
python_project/
├── api.py
├── mcp_server.py
├── main.py
├── index.html
├── tasks.json
├── README.md
```

---

## How to Run

### 1. Start Backend
```bash
python -m uvicorn api:app --reload
```

### 2. Open Frontend
Open `index.html` in your browser.

---

## API Endpoints
- POST /add → Add a task  
- GET /tasks → Get all tasks  
- DELETE /delete/{index} → Delete a task  
- GET /suggest → Get suggested task  
- GET /count → Get total tasks  

---

## MCP Integration
The project includes an MCP server exposing:

- Tools: add_task, list_tasks, delete_task, suggest_task  
- Resource: tasks://all  

---

## Future Improvements
- Add authentication (login system)  
- Replace JSON with database (MongoDB)  
- Improve UI using React  
- Deploy the application online  

---

## Author
Lakshmiprasannamchitta