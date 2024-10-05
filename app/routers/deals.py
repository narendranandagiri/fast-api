from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import deal as models
from ..schemas import deal as schemas

router = APIRouter()

@router.post("/deals/", response_model=schemas.Deal)
def create_deal(deal: schemas.DealCreate, db: Session = Depends(get_db)):
    db_deal = models.Deal(**deal.dict())
    db.add(db_deal)
    db.commit()
    db.refresh(db_deal)
    return db_deal

@router.get("/deals/", response_model=List[schemas.Deal])
def read_deals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    deals = db.query(models.Deal).offset(skip).limit(limit).all()
    return deals

@router.get("/deals/{deal_id}", response_model=schemas.Deal)
def read_deal(deal_id: int, db: Session = Depends(get_db)):
    deal = db.query(models.Deal).filter(models.Deal.id == deal_id).first()
    if deal is None:
        raise HTTPException(status_code=404, detail="Deal not found")
    return deal

@router.put("/deals/{deal_id}", response_model=schemas.Deal)
def update_deal(deal_id: int, deal: schemas.DealCreate, db: Session = Depends(get_db)):
    db_deal = db.query(models.Deal).filter(models.Deal.id == deal_id).first()
    if db_deal is None:
        raise HTTPException(status_code=404, detail="Deal not found")
    for key, value in deal.dict().items():
        setattr(db_deal, key, value)
    db.commit()
    db.refresh(db_deal)
    return db_deal

@router.delete("/deals/{deal_id}", response_model=schemas.Deal)
def delete_deal(deal_id: int, db: Session = Depends(get_db)):
    deal = db.query(models.Deal).filter(models.Deal.id == deal_id).first()
    if deal is None:
        raise HTTPException(status_code=404, detail="Deal not found")
    db.delete(deal)
    db.commit()
    return deal