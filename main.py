# FastAPI 엔트리

from fastapi import FastAPI
from auth.routes import router as auth_router
from models.user import Base
from db.session import engine
from routes.user import router as user_router

app = FastAPI()

Base.metadata.create_all(bind=engine)  # 테이블 생성

app.include_router(auth_router)

app.include_router(auth_router)
app.include_router(user_router)