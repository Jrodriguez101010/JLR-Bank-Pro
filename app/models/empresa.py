from sqlalchemy import Column, Integer, String, Boolean

from app.core.database import Base


class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, autoincrement=True)

    razon_social = Column(String(150), nullable=False)
    nombre_fantasia = Column(String(150))
    cuit = Column(String(13), unique=True)
    direccion = Column(String(200))
    localidad = Column(String(100))
    provincia = Column(String(100))
    telefono = Column(String(50))
    email = Column(String(150))

    activa = Column(Boolean, default=True)