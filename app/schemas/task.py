from pydantic import BaseModel
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: str
    deadline: datetime
    assigned_to: str

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True