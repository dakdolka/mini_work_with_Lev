from fastapi import FastAPI
from queries.orm import SyncORM
import uvicorn

from fastapi.middleware.cors import CORSMiddleware

# Настраиваем приложение FastAPI
app = FastAPI()

# Добавляем CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить запросы с любых источников
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить любые HTTP-методы (GET, POST и т.д.)
    allow_headers=["*"],  # Разрешить любые заголовки
)


@app.get("/add/{info}")  # отлавливание всех get запросов, начинающихся с слэша
def root(info: str, price: int):
    print(info)
    return SyncORM.add_info(info)

@app.get("/get_all")
def get_all():
    return {'ans': SyncORM.get_all_info()}


if __name__ == "__main__":
    SyncORM.create_tables()
    uvicorn.run("main:app", reload=True) # перезагружать при изменении