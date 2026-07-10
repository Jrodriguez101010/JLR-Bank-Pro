from sqlalchemy import (
    Boolean,
    Column,
    Float,
    ForeignKey,
    Integer,
    String
)

from sqlalchemy.orm import relationship

from app.core.database import Base


class CuentaBancaria(Base):

    __tablename__ = "cuentas_bancarias"

    id = Column(Integer, primary_key=True, autoincrement=True)

    cliente_id = Column(
        Integer,
        ForeignKey("clientes.id"),
        nullable=False
    )

    banco = Column(String(100), nullable=False)

    sucursal = Column(String(100))

    tipo_cuenta = Column(String(50))

    numero_cuenta = Column(String(50))

    cbu = Column(String(22))

    alias = Column(String(100))

    moneda = Column(String(20), default="ARS")

    saldo_inicial = Column(Float, default=0)

    activa = Column(Boolean, default=True)

    cliente = relationship("Cliente")