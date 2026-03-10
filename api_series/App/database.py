from httpx import get
from pymysql
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import Session, sessionmaker, declarative_base
from os import getenv
from dotenv import load_dotenv

load_dotenv()
def __criar_banco_se_nao_existir():
    # Cria o banco de dados se ele não existir
    connection = pymysql.connect(
        host=getenv('DB_HOST'),)

DATABASE_URL = f"""mysql+pymysql://{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@
{getenv('DB_HOST')}/{getenv('DB_NAME')}"""

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

Base = declarative_base()

#ingeção de dependência: injeta a sessão do banco de dados em cada requisição
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()