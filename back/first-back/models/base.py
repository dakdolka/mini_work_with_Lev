from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    echo = True # Вывод в консоль всех логов == действий бд