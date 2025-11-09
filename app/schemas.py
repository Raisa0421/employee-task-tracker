from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

# ---------------- EMPLOYEE SCHEMAS ----------------
class EmployeeBase(BaseModel):
    name: str = Field(..., min_length=1, description="Employee name is required")
    email: str = Field(..., min_length=1, description="Employee email is required")
    department: str = Field(..., min_length=1, description="Department is required")
    position: str = Field(..., min_length=1, description="Position is required")

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        from_attributes = True  
        
# ---------------- TASK SCHEMAS ----------------
class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, description="Task title is required")
    description: str = Field(..., min_length=1, description="Task description is required")
    due_date: date = Field(..., description="Due date is required")
    completed: bool = False
    employee_id: Optional[int] = Field(None, description="Employee ID (optional)")

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config:
        from_attributes = True 
