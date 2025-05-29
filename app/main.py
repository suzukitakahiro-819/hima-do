# app/main.py
from fastapi import FastAPI
from .database import engine, Base
import app.models  

app = FastAPI(title="HiMa-Do")

# アプリ起動時にテーブルを作成
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "HiMa-Do MVP success!"}