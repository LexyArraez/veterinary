from datetime import date
from pydantic import BaseModel
from typing import Optional


class PetBase(BaseModel):
    name: str
    species: str
    race: str
    date_of_birth: date
    customer_id: int


class PetCreate(PetBase):
    pass


class PetUpdate(BaseModel):
    name: Optional[str] = None
    species: Optional[str] = None
    race: Optional[str] = None
    date_of_birth: Optional[date] = None
    customer_id: Optional[int] = None

class PetResponse(PetBase):
    id_pets: int
    model_config = {"from_attributes": True}