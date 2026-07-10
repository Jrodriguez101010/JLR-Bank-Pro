from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Date,
    Boolean,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.core.database import Base


class Movimiento(Base):
    __tablename__ = "movimientos"

    id = Column(Integer, primary_key=True, autoincrement=True)

    cuenta_id = Column(
        Integer,
        ForeignKey("cuentas.id"),
        nullable=False
    )

    fecha = Column(Date, nullable=False)

    descripcion = Column(String(300), nullable=False)

    importe = Column(Float, nullable=False)

    saldo = Column(Float)

    tipo = Column(String(20))

    clasificacion = Column(String(100))

    observaciones = Column(String(300))

    procesado = Column(Boolean, default=False)

    cuenta = relationship(
        "Cuenta",
        back_populates="movimientos"
    )