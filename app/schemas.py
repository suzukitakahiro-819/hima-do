# app/schemas.py
from datetime import datetime
from pydantic import BaseModel

class ActivityHistoryBase(BaseModel):
    timestamp: datetime
    category: str

class ActivityHistoryCreate(ActivityHistoryBase):
    pass
    # ⇒ POST 時に受け取るフィールド
    #    追加で ID を受け取る必要がなければそのままでOK

class ActivityHistory(ActivityHistoryBase):
    id: int

    class Config:
        orm_mode = True
        # SQLAlchemy のモデルを Pydantic に読み込ませるときに必要

class FeedbackBase(BaseModel):
    activity_id: int
    liked: int  # 0 or 1

class FeedbackCreate(FeedbackBase):
    pass

class Feedback(FeedbackBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True