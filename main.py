from fastapi import FastAPI
from routers import candidatos
from db.database import Base,engine

Base.metadata.create_all(bind=engine)
app= FastAPI()

app.include_router(candidatos.candidatosrouter)


