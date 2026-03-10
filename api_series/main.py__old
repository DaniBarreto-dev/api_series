from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/itens/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/soma")
def soma(a : int, b:int):
    return{"resultado": a + b}

@app.get("/soma/{a}/{b}")
def soma(a : int, b:int):
    return{"resultado": a + b}
