from pydantic import BaseModel
from typing import Optional

class SerieSchema(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    ano_lancamento: int

    class config:
        from_atribute = True