from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.database.db_connection import Base


class VeterinarioSchema(Base):
    __tablename__ = "veterinarians"

    id_veterinarians: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    specialty: Mapped[str] = mapped_column(String(100), nullable=False)