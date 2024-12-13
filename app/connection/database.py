from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "postgresql://postgres:1234@localhost/db_ecommerce"  # Substitua com seus dados

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.engine = create_engine(DATABASE_URL)
            cls._instance.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=cls._instance.engine)
        return cls._instance

    def get_session(self):
        """Retorna uma sessão como um context manager."""
        return self.SessionLocal()  # Retorna a sessão para ser usada com 'with'

database = Database()  # Instância Singleton do banco de dados

Base = declarative_base()  # Base para criar as tabelas