from pydantic import BaseModel
from ..models.deal import DealStage

class DealBase(BaseModel):
    name: str
    value: float
    stage: DealStage

class DealCreate(DealBase):
    pass

class Deal(DealBase):
    id: int

    class Config:
        orm_mode = True