from app.models.movimiento import Movimiento
from app.repositories.movimiento_repository import MovimientoRepository


class MovimientoService:

    @staticmethod
    def listar(db):
        return MovimientoRepository.listar(db)

    @staticmethod
    def listar_por_cuenta(db, cuenta_id):
        return MovimientoRepository.listar_por_cuenta(
            db,
            cuenta_id
        )

    @staticmethod
    def buscar(db, texto):
        return MovimientoRepository.buscar(
            db,
            texto
        )

    @staticmethod
    def crear(db, datos):

        movimiento = Movimiento(
            cuenta_id=datos["cuenta_id"],
            fecha=datos["fecha"],
            descripcion=datos["descripcion"],
            importe=datos["importe"],
            saldo=datos.get("saldo"),
            tipo=datos.get("tipo"),
            clasificacion=datos.get("clasificacion"),
            observaciones=datos.get("observaciones"),
            procesado=datos.get("procesado", False)
        )

        return MovimientoRepository.crear(
            db,
            movimiento
        )

    @staticmethod
    def actualizar(db, movimiento_id, datos):

        movimiento = MovimientoRepository.obtener_por_id(
            db,
            movimiento_id
        )

        if movimiento is None:
            return None

        movimiento.fecha = datos["fecha"]
        movimiento.descripcion = datos["descripcion"]
        movimiento.importe = datos["importe"]
        movimiento.saldo = datos.get("saldo")
        movimiento.tipo = datos.get("tipo")
        movimiento.clasificacion = datos.get("clasificacion")
        movimiento.observaciones = datos.get("observaciones")
        movimiento.procesado = datos.get("procesado", False)

        return MovimientoRepository.actualizar(
            db,
            movimiento
        )

    @staticmethod
    def eliminar(db, movimiento_id):

        movimiento = MovimientoRepository.obtener_por_id(
            db,
            movimiento_id
        )

        if movimiento:
            MovimientoRepository.eliminar(
                db,
                movimiento
            )