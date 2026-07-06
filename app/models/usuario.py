from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

from app.core.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)

    nombre = Column(String(80), nullable=False)

    apellido = Column(String(80), nullable=False)

    usuario = Column(String(40), unique=True, nullable=False)

    password = Column(String(255), nullable=False)

    email = Column(String(120), unique=True)

    rol = Column(String(30), nullable=False)

    activo = Column(Boolean, default=True)

    fecha_creacion = Column(DateTime(timezone=True),
                            server_default=func.now())