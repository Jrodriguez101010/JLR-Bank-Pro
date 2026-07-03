from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Empresa(Base):
    __tablename__ = "empresas"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)