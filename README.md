## Setup / Installation

1. **Clone the repository**
```bash
git clone https://github.com/Raisa0421/employee-task-tracker.git
cd employee-task-tracker
python -m venv venv
venv\Scripts\activate       
pip install -r requirements.txt
uvicorn app.main:app --reload.

 ##Tech stack used
- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite / PostgreSQL
- Pydantic
- python-dateutil
- python-multipart

## Assumptions / Bonus Features

- Assumes that each task is assigned to a single employee.
- Default analytics shows upcoming tasks for the next 7 days.
- Bonus Features:
  - Analytics endpoints for tasks per employee, completed tasks, and upcoming tasks.
  - Interactive Swagger API documentation at `/docs`.

  
  

