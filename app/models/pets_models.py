from datetime import date
from typing import TYPE_CHECKING
from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.db_connection import Base


if TYPE_CHECKING:
    from app.models.customers_models import CustomerModel

class PetsModel(Base):
    __tablename__ = "pets"

    id_pets: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    species: Mapped[str] = mapped_column(String(50), nullable=False)
    race: Mapped[str] = mapped_column(String(50), nullable=False)
    date_of_birth: Mapped[date] = mapped_column(Date, nullable=False)


    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.customer_id"), nullable=False)
    customer: Mapped["CustomerModel"] = relationship(
        "CustomerModel",
        back_populates="pets"
    )