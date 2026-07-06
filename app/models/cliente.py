from sqlalchemy import Column, Integer, String
from app.core.database import Base


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    apellido = Column(String(100), nullable=False)
    nombre = Column(String(100), nullable=False)
    dni = Column(String(20), unique=True, nullable=False)
    cuit = Column(String(20))
    telefono = Column(String(30))
    email = Column(String(150))
    domicilio = Column(String(200))
    ciudad = Column(String(100))
    provincia = Column(String(100))
    codigo_postal = Column(String(20))
    estado = Column(String(20), default="ACTIVO")