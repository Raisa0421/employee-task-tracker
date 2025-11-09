# Employee Task Tracker with Analytics - Backend

## Description
This is the backend API for the Employee Task Tracker with Analytics project, built using **FastAPI**.  
It allows you to manage employees and tasks, and provides analytics on task assignments, completed tasks, and upcoming tasks.  
Interactive API documentation is available at `/docs`.

**Technologies Used:** Python, FastAPI, SQLAlchemy, Pydantic, SQLite/PostgreSQL, python-dateutil.

---

## Features
- **Employee Management:** Create, read, and delete employees
- **Task Management:** Create, read, and delete tasks
- **Analytics:**
  - Tasks assigned per employee
  - Completed tasks per employee
  - Upcoming tasks within a given number of days
- Interactive API documentation via Swagger at `/docs`
- Data validation using Pydantic models

---
#setup
Create a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Run the application:
```bash
uvicorn app.main:app --reload
```
Open the API documentation in a browser:
http://localhost:8000/docs

---
##Tech stack
- Python 
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite/PostgreSQL
- python-dateutil

## Usage
### Employees
- POST /employees/ - Create a new employee
- GET /employees/ - Get all employees
- DELETE /employees/{employee_id} - Delete a specific employee

### Tasks
- POST /tasks/ - Create a new task
- GET /tasks/ - Get all tasks
- DELETE /tasks/{task_id} - Delete a specific task

### Analytics
- GET /analytics/tasks_per_employee/ - Get number of tasks assigned to each employee
- GET /analytics/completed_tasks_per_employee/ - Get number of completed tasks per employee
- GET /analytics/upcoming_tasks/ - Get upcoming tasks within a given number of days

##screenshots


## Project structure
employee-task-tracker
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── utils.py
│   └── routers
│       ├── __init__.py
│       ├── analytics.py
│       ├── employees.py
│       ├── tasks.py
│       └── departments.py
├── README.md
├── requirements.txt



## License



