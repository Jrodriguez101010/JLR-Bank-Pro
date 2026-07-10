from sqlalchemy import or_

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
            .filter(Movimiento.cuenta_id == cuenta_id)
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
    def eliminar(db, movimiento):

        db.delete(movimiento)
        db.commit()