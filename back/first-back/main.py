from fastapi import FastAPI
from queries.orm import SyncORM
import uvicorn

app = FastAPI() #наше приложение

@app.get("localhost/add/{info}")  # отлавливание всех get запросов, начинающихся с слэша
async def root(info: str, price: int):
    print(info)
    return SyncORM.add_info(info)




if __name__ == "__main__":
    SyncORM.create_tables()
    uvicorn.run("main:app", reload=True) # перезагружать при изменении