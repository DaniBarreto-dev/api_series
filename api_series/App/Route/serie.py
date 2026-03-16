from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from App.Schema.database import get_db
from App.model.serie import Serie
from App.Schema.serie import SerieSchema

router = APIRouter()

@router.post("/series")
async def criar_serie(dados: SerieSchema, db: Session = Depends(get_db)):
    nova_serie = Serie(**dados.model_dump())
    db.add(nova_serie)
    db.commit()
    db.refresh(nova_serie)
    return nova_serie


@router.put("/series/{serie_id}")
def atualizar_serie(serie_id: int, dados: SerieSchema, db: Session = Depends(get_db)):

    serie_db = db.query(Serie).filter(Serie.id == serie_id).first()

    if not serie_db:
        raise HTTPException(status_code=404, detail="Série não encontrada")

    serie_db.titulo = dados.titulo
    serie_db.descricao = dados.descricao
    serie_db.ano_lancamento = dados.ano_lancamento

    db.commit()
    db.refresh(serie_db)

    return serie_db


@router.delete("/series/{serie_id}")
def deletar_serie(serie_id: int, db: Session = Depends(get_db)):

    serie_db = db.query(Serie).filter(Serie.id == serie_id).first()

    if not serie_db:
        raise HTTPException(status_code=404, detail="Série não encontrada")

    db.delete(serie_db)
    db.commit()

    return {"mensagem": "Série deletada com sucesso"}