from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.database.db_connection import Base


class CustomerModel(Base):
    __tablename__ = "customers"

    customer_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(150), nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=False)
    document_type: Mapped[str] = mapped_column(String(30), nullable=False)
    document_number: Mapped[str] = mapped_column(String(30), nullable=False)