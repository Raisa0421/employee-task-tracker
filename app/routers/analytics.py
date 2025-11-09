from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from .. import crud, schemas, models
from ..database import get_db
from ..utils import productivity_by_month

router = APIRouter()

@router.get("/department-summary", response_model=List[schemas.DepartmentSummary])
def department_summary(db: Session = Depends(get_db)):
    data = crud.department_summary(db)
    return data

@router.get("/top-performers", response_model=List[schemas.TopPerformer])
def top_performers(limit: int = 5, db: Session = Depends(get_db)):
    data = crud.top_performers(db, limit)
    return data

@router.get("/pending-tasks", response_model=List[schemas.TaskRead])
def pending_tasks(db: Session = Depends(get_db)):
    tasks = crud.pending_tasks(db)
    return tasks

@router.get("/productivity-trend")
def productivity_trend(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return productivity_by_month(tasks)
