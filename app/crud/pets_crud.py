from sqlalchemy.orm import Session
from app.models.pets_models import PetsModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app.schemas.pets_schema import PetCreate, PetUpdate


def create_pet(db: Session, pet_in: PetCreate):
    try:
        db_pet = PetsModel(**pet_in.model_dump())
        db.add(db_pet)
        db.commit()
        db.refresh(db_pet)
        return db_pet
    except IntegrityError as e:
        db.rollback()
        raise ValueError("El ID del cliente (dueño) proporcionado no existe.") from e
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError("Error interno en la base de datos al registrar la mascota.") from e



def get_pets(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(PetsModel).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        raise RuntimeError("Error al consultar las mascotas en la base de datos.") from e


def get_pet_by_id(db: Session, id_pets: int):
    try:
        return db.query(PetsModel).filter(PetModel.id_pets == id_pets).first()
    except SQLAlchemyError as e:
        raise RuntimeError("Error al consultar la mascota en la base de datos.") from e


def update_pet(db: Session, id_pets: int, pet_in: PetUpdate):
    db_pet = get_pet_by_id(db, id_pets)
    if not db_pet:
        return None

    try:
        update_data = pet_in.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_pet, key, value)

        db.commit()
        db.refresh(db_pet)
        return db_pet
    except IntegrityError as e:
        db.rollback()
        raise ValueError("No se pudo actualizar: El ID del dueño asignado no existe.") from e
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError("Error interno al intentar actualizar la mascota.") from e


def delete_pet(db: Session, id_pets: int):
    db_pet = get_pet_by_id(db, id_pets)
    if not db_pet:
        return None

    try:
        db.delete(db_pet)
        db.commit()
        return db_pet
    except SQLAlchemyError as e:
        db.rollback()
        raise RuntimeError("Error interno al intentar eliminar la mascota.") from e