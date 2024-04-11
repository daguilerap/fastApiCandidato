from fastapi import APIRouter, HTTPException, status
from db.database import Session
from db.schema.candidato import Candidato
from db.models.candidatosMoldel import candidatosModel



candidatosrouter = APIRouter(prefix="/candidato", tags=["candidatos"],
                          responses={status.HTTP_404_NOT_FOUND: {"mesage": "No encontrado"}})

@candidatosrouter.post("/", response_model=Candidato, status_code=status.HTTP_201_CREATED)
async def create_candidato(candidato: Candidato):
    db=Session()
    db_candidato = candidatosModel(**candidato.dict())
    if db.query(candidatosModel).filter(candidatosModel.dni == candidato.dni).first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El candidato ya existe")

        # Agrega el nuevo candidato a la base de datos
    db.add(db_candidato)
    db.commit()
    db.refresh(db_candidato)

    return db_candidato