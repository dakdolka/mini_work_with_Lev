# В этом файле описываем базу данных

from models.base import Base # Base - класс бд
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text 

class Table(Base): # Класс таблицы
    __tablename__ = 'table' # имя таблицы

    # Создание колонок - имя: обозначение типа = дополнительные атрибуты
    id: Mapped[int] = mapped_column(primary_key=True) # id (имя колонки) - колонка таблицы с типом данных int, primary_key - обозначение уникального ключа
    info: Mapped[str] = mapped_column(Text) # mapped_column() - функция колонки | Text - тип данных