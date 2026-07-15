from app.services.tipo_movimiento_service import TipoMovimientoService
from app.services.clasificador_service import ClasificadorService


class NormalizadorMovimientoService:

    @staticmethod
    def normalizar(movimiento):

        credito = movimiento.get("credito", 0) or 0
        debito = movimiento.get("debito", 0) or 0

        importe = TipoMovimientoService.normalizar_importe(
            credito,
            debito
        )

        descripcion = movimiento.get(
            "descripcion",
            ""
        ).strip()

        return {

            "fecha": movimiento.get("fecha"),

            "descripcion": descripcion,

            "importe": importe,

            "saldo": movimiento.get("saldo"),

            "tipo": TipoMovimientoService.obtener_tipo(
                importe
            ),

            "clasificacion": ClasificadorService.clasificar(
                descripcion
            ),

            "observaciones": None,

            "procesado": False

        }

    @staticmethod
    def normalizar_lista(movimientos):

        return [
            NormalizadorMovimientoService.normalizar(m)
            for m in movimientos
        ]