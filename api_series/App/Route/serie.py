from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from App.Schema.database import get_db
from App.model.serie import Serie
from App.Schema.serie import SerieSchema

serie = APIRouter()

@serie.post("/")
async def criar_serie(dados: SerieSchema, db: Session = Depends(get_db)):
    nova_serie = Serie(**dados.model_dump())
    db.add(nova_serie)
    db.commit()
    db.refresh(nova_serie)
    return nova_serie