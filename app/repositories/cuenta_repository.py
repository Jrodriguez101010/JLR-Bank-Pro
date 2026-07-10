from sqlalchemy import or_

from app.models.cuenta_bancaria import CuentaBancaria


class CuentaRepository:

    @staticmethod
    def listar(db):
        return (
            db.query(CuentaBancaria)
            .filter(CuentaBancaria.activa == True)
            .order_by(
                CuentaBancaria.banco,
                CuentaBancaria.numero_cuenta
            )
            .all()
        )

    @staticmethod
    def listar_por_cliente(db, cliente_id):
        return (
            db.query(CuentaBancaria)
            .filter(
                CuentaBancaria.cliente_id == cliente_id,
                CuentaBancaria.activa == True
            )
            .order_by(CuentaBancaria.banco)
            .all()
        )

    @staticmethod
    def obtener_por_id(db, cuenta_id):
        return (
            db.query(CuentaBancaria)
            .filter(CuentaBancaria.id == cuenta_id)
            .first()
        )

    @staticmethod
    def buscar(db, texto):

        texto = f"%{texto}%"

        return (
            db.query(CuentaBancaria)
            .filter(
                CuentaBancaria.activa == True,
                or_(
                    CuentaBancaria.banco.like(texto),
                    CuentaBancaria.numero_cuenta.like(texto),
                    CuentaBancaria.cbu.like(texto),
                    CuentaBancaria.alias.like(texto)
                )
            )
            .order_by(CuentaBancaria.banco)
            .all()
        )

    @staticmethod
    def crear(db, cuenta):

        db.add(cuenta)
        db.commit()
        db.refresh(cuenta)

        return cuenta

    @staticmethod
    def actualizar(db, cuenta):

        db.commit()
        db.refresh(cuenta)

        return cuenta

    @staticmethod
    def desactivar(db, cuenta):

        cuenta.activa = False

        db.commit()

        return cuenta