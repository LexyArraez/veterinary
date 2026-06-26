from pydantic import BaseModel, EmailStr


class CustomerBase(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    phone: str
    document_type: str
    document_number: str


class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    customer_id: int

    model_config = {"from_attributes": True}