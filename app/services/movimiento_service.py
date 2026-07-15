from app.models.movimiento import Movimiento
from app.repositories.movimiento_repository import MovimientoRepository


class MovimientoService:

    @staticmethod
    def listar(db):
        return MovimientoRepository.listar(db)

    @staticmethod
    def obtener_por_id(db, movimiento_id):
        return MovimientoRepository.obtener_por_id(
            db,
            movimiento_id
        )

    @staticmethod
    def listar_por_cuenta(
        db,
        cuenta_id
    ):
        return MovimientoRepository.listar_por_cuenta(
            db,
            cuenta_id
        )

    @staticmethod
    def buscar(
        db,
        texto
    ):
        return MovimientoRepository.buscar(
            db,
            texto
        )

    @staticmethod
    def crear(
        db,
        datos
    ):

        existente = MovimientoRepository.existe(
            db=db,
            cuenta_id=datos["cuenta_id"],
            fecha=datos["fecha"],
            descripcion=datos["descripcion"],
            importe=datos["importe"]
        )

        if existente:
            return existente

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
    def actualizar(
        db,
        movimiento_id,
        datos
    ):

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
        movimiento.procesado = datos.get(
            "procesado",
            False
        )

        return MovimientoRepository.actualizar(
            db,
            movimiento
        )

    @staticmethod
    def eliminar(
        db,
        movimiento_id
    ):
        return MovimientoRepository.eliminar(
            db,
            movimiento_id
        )

    @staticmethod
    def importar_movimientos(
        db,
        cuenta_id,
        movimientos
    ):

        importados = 0
        duplicados = 0

        for mov in movimientos:

            datos = {

                "cuenta_id": cuenta_id,

                "fecha": mov["fecha"],

                "descripcion": mov["descripcion"],

                "importe": mov["importe"],

                "saldo": mov.get("saldo"),

                "tipo": mov.get("tipo"),

                "clasificacion": mov.get("clasificacion"),

                "observaciones": mov.get("observaciones"),

                "procesado": mov.get(
                    "procesado",
                    False
                )

            }

            existente = MovimientoRepository.existe(
                db=db,
                cuenta_id=datos["cuenta_id"],
                fecha=datos["fecha"],
                descripcion=datos["descripcion"],
                importe=datos["importe"]
            )

            if existente:
                duplicados += 1
                continue

            MovimientoService.crear(
                db,
                datos
            )

            importados += 1

        return {
            "importados": importados,
            "duplicados": duplicados,
            "total": len(movimientos)
        }

    @staticmethod
    def reprocesar_clasificaciones(
        db,
        cuenta_id
    ):

        from app.services.clasificador_service import ClasificadorService

        movimientos = MovimientoRepository.listar_por_cuenta(
            db,
            cuenta_id
        )

        actualizados = 0

        for movimiento in movimientos:

            nueva = ClasificadorService.clasificar(
                movimiento.descripcion
            )

            if movimiento.clasificacion != nueva:

                movimiento.clasificacion = nueva

                MovimientoRepository.actualizar(
                    db,
                    movimiento
                )

                actualizados += 1

        return {
            "actualizados": actualizados,
            "total": len(movimientos)
        }

    @staticmethod
    def contar(db):
        return MovimientoRepository.contar(db)

    @staticmethod
    def contar_por_cuenta(
        db,
        cuenta_id
    ):
        return MovimientoRepository.contar_por_cuenta(
            db,
            cuenta_id
        )