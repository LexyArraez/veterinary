from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.db_connection import get_db
from app.schemas.pets_schema import PetCreate, PetUpdate, PetResponse
from app.crud import pets_crud

router = APIRouter(prefix="/pets", tags=["Pets"])

@router.post("/", response_model=PetResponse, status_code=status.HTTP_201_CREATED)
def crear_mascota(pet_in: PetCreate, db: Session = Depends(get_db)):
    try:
        return pets_crud.create_pet(db=db, pet_in=pet_in)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))
    except RuntimeError as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))


@router.get("/", response_model=list[PetResponse])
def listar_mascotas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        return pets_crud.get_pets(db=db, skip=skip, limit=limit)
    except RuntimeError as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))


@router.get("/{id_pets}", response_model=PetResponse)
def obtener_mascota(id_pets: int, db: Session = Depends(get_db)):
    try:
        db_pet = pets_crud.get_pet_by_id(db=db, id_pets=id_pets)
        if not db_pet:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mascota no encontrada.")
        return db_pet
    except RuntimeError as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))



@router.put("/{id_pets}", response_model=PetResponse)
def actualizar_mascota(id_pets: int, pet_in: PetUpdate, db: Session = Depends(get_db)):
    try:
        db_pet = pets_crud.update_pet(db=db, id_pets=id_pets, pet_in=pet_in)
        if not db_pet:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mascota no encontrada para actualizar.")
        return db_pet
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))
    except RuntimeError as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))



@router.delete("/{id_pets}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_mascota(id_pets: int, db: Session = Depends(get_db)):
    try:
        db_pet = pets_crud.delete_pet(db=db, id_pets=id_pets)
        if not db_pet:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mascota no encontrada para eliminar.")
        return None
    except RuntimeError as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))