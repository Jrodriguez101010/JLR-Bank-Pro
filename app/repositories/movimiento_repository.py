from sqlalchemy import or_, and_

from app.models.movimiento import Movimiento


class MovimientoRepository:

    @staticmethod
    def listar(db):
        return (
            db.query(Movimiento)
            .order_by(
                Movimiento.fecha.desc(),
                Movimiento.id.desc()
            )
            .all()
        )

    @staticmethod
    def obtener_por_id(db, movimiento_id):
        return (
            db.query(Movimiento)
            .filter(Movimiento.id == movimiento_id)
            .first()
        )

    @staticmethod
    def listar_por_cuenta(db, cuenta_id):
        return (
            db.query(Movimiento)
            .filter(
                Movimiento.cuenta_id == cuenta_id
            )
            .order_by(
                Movimiento.fecha.desc(),
                Movimiento.id.desc()
            )
            .all()
        )

    @staticmethod
    def buscar(db, texto):

        texto = f"%{texto}%"

        return (
            db.query(Movimiento)
            .filter(
                or_(
                    Movimiento.descripcion.like(texto),
                    Movimiento.clasificacion.like(texto)
                )
            )
            .order_by(
                Movimiento.fecha.desc(),
                Movimiento.id.desc()
            )
            .all()
        )

    @staticmethod
    def existe(
        db,
        cuenta_id,
        fecha,
        descripcion,
        importe
    ):

        return (
            db.query(Movimiento)
            .filter(
                and_(
                    Movimiento.cuenta_id == cuenta_id,
                    Movimiento.fecha == fecha,
                    Movimiento.descripcion == descripcion,
                    Movimiento.importe == importe
                )
            )
            .first()
        )

    @staticmethod
    def crear(db, movimiento):

        db.add(movimiento)

        db.commit()

        db.refresh(movimiento)

        return movimiento

    @staticmethod
    def actualizar(db, movimiento):

        db.commit()

        db.refresh(movimiento)

        return movimiento

    @staticmethod
    def eliminar(db, movimiento_id):

        movimiento = (
            db.query(Movimiento)
            .filter(
                Movimiento.id == movimiento_id
            )
            .first()
        )

        if movimiento:

            db.delete(movimiento)

            db.commit()

            return True

        return False

    @staticmethod
    def contar(db):

        return (
            db.query(Movimiento)
            .count()
        )

    @staticmethod
    def contar_por_cuenta(
        db,
        cuenta_id
    ):

        return (
            db.query(Movimiento)
            .filter(
                Movimiento.cuenta_id == cuenta_id
            )
            .count()
        )