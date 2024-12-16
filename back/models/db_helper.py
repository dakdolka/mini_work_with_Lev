# Создаем движок == подключение к бд и фабрику сессий
# Фабрика сессий - исполнитель запросов
# * == клишейная строка

from config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DB_Helper:
    def __init__(self):
        self.engine = create_engine(settings.db_url) #*
        self.session_factory = sessionmaker(bind=self.engine) #*

db_helper = DB_Helper()