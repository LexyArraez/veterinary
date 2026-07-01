from sqlalchemy import String, Date, ForeignKey
from datetime import date
from sqlalchemy.orm import Mapped, mapped_column
from app.database.db_connection import Base


class HistoriaClinicaSchema(Base):
    __tablename__ = "medical_record"

    id_medical_record: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_pets: Mapped[int] = mapped_column(ForeignKey("pets.id_ets"), unique=True, nullable=False)
    creation_date: Mapped[date] = mapped_column(Date, nullable=False)
    general_description: Mapped[str] = mapped_column(String(250), nullable=False)