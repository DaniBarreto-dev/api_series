from fastapi import FastAPI
from App.Route.serie import router
from App.Schema.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
async def health_check():
    return {"status": "API Online"}

