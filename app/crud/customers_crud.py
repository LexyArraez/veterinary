from sqlalchemy.orm import Session
from app.models.customers_models import CustomerModel
from app.schemas.customers_schema import CustomerCreate, CustomerUpdate


def create_customer(db: Session, customer_in: CustomerCreate):
    db_customer = CustomerModel(**customer_in.model_dump())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer



def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CustomerModel).offset(skip).limit(limit).all()


def get_customer_by_id(db: Session, customer_id: int):
    return db.query(CustomerModel).filter(CustomerModel.customer_id == customer_id).first()


def update_customer(db: Session, customer_id: int, customer_in: CustomerUpdate):
    db_customer = get_customer_by_id(db, customer_id)
    if not db_customer:
        return None


    update_data = customer_in.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_customer, key, value)

    db.commit()
    db.refresh(db_customer)
    return db_customer



def delete_customer(db: Session, customer_id: int):
    db_customer = get_customer_by_id(db, customer_id)
    if db_customer:
        db.delete(db_customer)
        db.commit()
    return db_customer