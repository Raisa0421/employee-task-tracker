from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date, timedelta
from fastapi.middleware.cors import CORSMiddleware


from app import models, crud, schemas
from app.database import Base, engine, SessionLocal

# ✅ Create tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Task Tracker with Analytics")

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict later to specific origins like ["http://localhost:8000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------- ROOT ----------------
@app.get("/")
def root():
    return {"message": "Employee Task Tracker API. Open /docs for interactive API docs."}

# ---------------- EMPLOYEE ROUTES ----------------
@app.post("/employees/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)

@app.get("/employees/", response_model=list[schemas.Employee])
def read_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = crud.delete_employee(db, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}

# ---------------- TASK ROUTES ----------------
@app.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)

@app.get("/tasks/", response_model=list[schemas.Task])
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.delete_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}

# ---------------- ANALYTICS ----------------
@app.get("/analytics/tasks_per_employee/")
def tasks_per_employee(db: Session = Depends(get_db)):
    """
    Return number of tasks assigned to each employee
    """
    result = db.query(
        models.Employee.name,
        func.count(models.Task.id).label("task_count")
    ).join(models.Task, models.Task.employee_id == models.Employee.id, isouter=True
    ).group_by(models.Employee.id).all()
    return [{"employee": r[0], "task_count": r[1]} for r in result]

@app.get("/analytics/completed_tasks_per_employee/")
def completed_tasks_per_employee(db: Session = Depends(get_db)):
    """
    Return number of completed tasks per employee
    """
    result = db.query(
        models.Employee.name,
        func.count(models.Task.id).label("completed_count")
    ).join(models.Task, models.Task.employee_id == models.Employee.id
    ).filter(models.Task.completed == True
    ).group_by(models.Employee.id).all()
    return [{"employee": r[0], "completed_tasks": r[1]} for r in result]

@app.get("/analytics/upcoming_tasks/")
def upcoming_tasks(days: int = 7, db: Session = Depends(get_db)):
    """
    Return tasks due in the next X days (default 7)
    """
    today = date.today()
    end_date = today + timedelta(days=days)
    tasks = db.query(models.Task).filter(
        models.Task.due_date >= today,
        models.Task.due_date <= end_date
    ).all()
    return tasks
