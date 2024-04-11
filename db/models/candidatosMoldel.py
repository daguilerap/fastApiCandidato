from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db.database import  Base

class candidatosModel(Base):
    __tablename__ = "candidatos"

    id = Column(Integer, primary_key=True, index=True)
    dni = Column(String, unique=True, index=True)
    nombre = Column(String, index=True)
    apellido = Column(String, index=True)