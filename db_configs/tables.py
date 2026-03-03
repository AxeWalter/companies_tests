from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base
import dotenv
import os

dotenv.load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database_name = os.getenv("DB_NAME")

url = f"postgresql://{user}:{password}@{host}:{port}/{database_name}"
engine = create_engine(url)
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nome = Column(String)

Base.metadata.create_all(engine)