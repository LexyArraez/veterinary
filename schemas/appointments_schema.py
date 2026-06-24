from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database.db_connection import Base


class CitaSchema(Base):
    __tablename__ = "appointments"

    id_appointments: Mapped[int] = mapped_column(primary_key=True, index=True)
    id_pets: Mapped[int] = mapped_column(ForeignKey("id.pets"), nullable=False)
    id_veterinarians: Mapped[int] = mapped_column(ForeignKey("id.veterinarians"), nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False)