from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from .database import Base

class ActivityHistory(Base):
    __tablename__ = "activity_history"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, index=True)
    category = Column(String, index=True)

class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    activity_id = Column(Integer, index=True)
    liked = Column(Integer)  # bad=0, good=1
    timestamp = Column(DateTime)