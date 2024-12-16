from fastapi import FastAPI
from queries.orm import SyncORM
import uvicorn
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

# Настраиваем приложение FastAPI
app = FastAPI()

# Добавляем CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://dakdolka.github.io/mini_work_with_Lev"],  # Разрешить запросы с любых источников
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить любые HTTP-методы (GET, POST и т.д.)
    allow_headers=["*"],  # Разрешить любые заголовки
)

class Info(BaseModel):
    info: str


@app.post("/add/")  # отлавливание всех get запросов, начинающихся с слэша
def root(info: Info):
    SyncORM.add_info(info.info)


@app.get("/get_all/")
def get_all():
    return {'ans': SyncORM.get_all_info()}


if __name__ == "__main__":
    SyncORM.create_tables()
    uvicorn.run("main:app", reload=True) # перезагружать при изменении