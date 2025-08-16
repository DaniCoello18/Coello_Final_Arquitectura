from pydantic import BaseModel, Field
from typing import List

class Objeto(BaseModel):
    nombre: str = Field(..., min_length=1)
    peso: int = Field(..., ge=0)
    ganancia: int = Field(..., ge=0)

class OptRequest(BaseModel):
    capacidad: int = Field(..., ge=0)
    objetos: List[Objeto]

class OptResponse(BaseModel):
    seleccionados: List[str]
    ganancia_total: int
    peso_total: int
