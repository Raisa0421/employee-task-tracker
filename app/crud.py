from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError  
from fastapi import HTTPException
from app import models, schemas

# ---------------- EMPLOYEE CRUD ----------------
def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(
        name=employee.name,
        email=employee.email,
        department=employee.department,
        position=employee.position
    )
    try:
        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)
        return db_employee
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already exists. Please use a different email.")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")


def get_employees(db: Session):
    try:
        return db.query(models.Employee).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching employees: {str(e)}")


def delete_employee(db: Session, employee_id: int):
    try:
        employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")

        db.delete(employee)
        db.commit()
        return {"message": "Employee deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting employee: {str(e)}")


# ---------------- TASK CRUD ----------------
def create_task(db: Session, task: schemas.TaskCreate):
    try:
        # Verify the employee exists only if employee_id is provided
        if task.employee_id is not None:
            employee = db.query(models.Employee).filter(models.Employee.id == task.employee_id).first()
            if not employee:
                raise HTTPException(status_code=404, detail="Employee not found for this task")

        db_task = models.Task(
            title=task.title,
            description=task.description,
            due_date=task.due_date,
            completed=task.completed,
            employee_id=task.employee_id
        )
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating task: {str(e)}")


def get_tasks(db: Session):
    try:
        return db.query(models.Task).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching tasks: {str(e)}")


def delete_task(db: Session, task_id: int):
    try:
        task = db.query(models.Task).filter(models.Task.id == task_id).first()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        db.delete(task)
        db.commit()
        return {"message": "Task deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting task: {str(e)}")
