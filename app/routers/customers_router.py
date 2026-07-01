from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.db_connection import get_db
from app.schemas.customers_schema import CustomerCreate, CustomerRead, CustomerUpdate
from app.crud import customers_crud

router = APIRouter(prefix="/customers", tags=["Customers"])

#crear cliente
@router.post("/", response_model=CustomerRead, status_code=status.HTTP_201_CREATED)
def create_customer(customer_in: CustomerCreate, db: Session = Depends(get_db)):
    return customers_crud.create_customer(db=db, customer_in=customer_in)

#listar clientes
@router.get("/", response_model=list[CustomerRead])
def list_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return customers_crud.get_customers(db=db, skip=skip, limit=limit)

#obtener cliente
@router.get("/{customer_id}", response_model=CustomerRead)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = customers_crud.get_customer_by_id(db=db, customer_id=customer_id)
    if not db_customer:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return db_customer

#actualizar_cliente
@router.put("/{customer_id}", response_model=CustomerRead)
def update_customer(customer_id: int, customer_in: CustomerUpdate, db: Session = Depends(get_db)):
    db_customer = customers_crud.update_customer(db=db, customer_id=customer_id, customer_in=customer_in)
    if not db_customer:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return db_customer

@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = customers_crud.get_customer_by_id(db=db, customer_id=customer_id)
    if not db_customer:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    customers_crud.delete_customer(db=db, customer_id=customer_id)
    return None