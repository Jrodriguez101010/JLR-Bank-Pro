from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.core.database import Base


class Cuenta(Base):
    __tablename__ = "cuentas"

    id = Column(Integer, primary_key=True, autoincrement=True)

    cliente_id = Column(
        Integer,
        ForeignKey("clientes.id"),
        nullable=False
    )

    banco = Column(String(100), nullable=False)

    tipo_cuenta = Column(String(50), nullable=False)

    numero = Column(String(50), nullable=False)

    cbu = Column(String(30))

    alias = Column(String(100))

    moneda = Column(String(20), default="ARS")

    activa = Column(Boolean, default=True)

    movimientos = relationship(
        "Movimiento",
        back_populates="cuenta",
        cascade="all, delete-orphan"
    )