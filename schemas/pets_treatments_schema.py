from datetime import date
from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database.db_connection import Base


class MascotaTratamientoSchema(Base):
    __tablename__ = "pet_treatment"

    pet_treatment_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_pets: Mapped[int] = mapped_column(ForeignKey("id.pets"), nullable=False)
    treatment_id: Mapped[int] = mapped_column(ForeignKey("treatment_id"), nullable=False)
    start_date: Mapped[date] = mapped_column(Date, nullable=False)
    end_date: Mapped[date] = mapped_column(Date, nullable=False)
    dose: Mapped[str] = mapped_column(String(100), nullable=False)