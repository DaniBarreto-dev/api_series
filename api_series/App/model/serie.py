from sqlalchemy import Column, Integer, String
from App.Schema.database import Base

class Serie(Base):
    __tablename__ = 'series'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    descrição = Column(String(255))
    ano_lancamento = Column(Integer)