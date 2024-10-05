from sqlalchemy import Column, Integer, String, Float, Enum
from ..database import Base
import enum

class DealStage(enum.Enum):
    lead = "lead"
    proposal = "proposal"
    negotiation = "negotiation"
    closed = "closed"

class Deal(Base):
    __tablename__ = "deals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    value = Column(Float)
    stage = Column(Enum(DealStage))