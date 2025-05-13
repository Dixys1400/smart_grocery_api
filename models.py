from sqlalchemy import Column, Integer, String, Boolean, DateTime
from database import Base
from datetime import datetime

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String, index=True)
    purchased = Column(Boolean, nullable=False, default=False)
    added_at = Column(DateTime, default=datetime.utcnow)
    purchase_count = Column(Integer, default=0)
