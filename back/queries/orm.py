# Файл для создания методов взаимодействия с бд
# * == клишейная строка

from sqlalchemy import select
from models.table import Table # Если таблиц несколько, пеерчисляем через запятую
from models.base import Base
from models.db_helper import db_helper

class SyncORM: # Класс со всеми запросами

    @staticmethod # Позволяет юзать метод без создания объекта класса 
    def create_tables(): # Создание всех ранее описанных таблиц в бд
        Base.metadata.create_all(db_helper.engine) #* Так надо

    @staticmethod
    def get_info_by_id(id: int): # Получение чего-то по id, если будет передано не int - исключение
        with db_helper.session_factory() as session: # Как open() но не файл, а сессия
            query = select(Table.info).where(Table.id == id) # Создаем запрос
            #select - выбрать: в скобках указываем класс таблицы и как поле конкретно либо соло класс
            #where - фильтр
            res = session.execute(query).scalars().all() #* Лутаем данные 
        return res

    @staticmethod
    def add_info(info: str):
        with db_helper.session_factory() as session:
            table = Table(info=info) # Так можно обращаться к конкретному атрибуту, мы в объект класса Table закидываем нашу info,
                                    # которую получили в функции
            session.add(table) #* Закидываем обновленные данные в бд
            session.commit() #* Сохраняем и закрываем

    @staticmethod
    def get_all_info():
        with db_helper.session_factory() as session:
            query = select(Table.info)
            res = session.execute(query).scalars().all()
            print(res)
        return res