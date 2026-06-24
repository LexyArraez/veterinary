from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column
from app.database.db_connection import Base


class TratamientoSchema(Base):
    __tablename__ = "treatments"

    treatment_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    treatment_description: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)