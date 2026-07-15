from app.pdf.motor_importacion import MotorImportacion
from app.services.movimiento_service import MovimientoService
from app.services.normalizador_movimiento_service import (
    NormalizadorMovimientoService
)


class ImportadorService:

    @staticmethod
    def importar_pdf(
        db,
        cuenta_id,
        ruta_pdf
    ):

        try:

            resultado = MotorImportacion.importar(ruta_pdf)

            if not resultado:

                return {
                    "ok": False,
                    "mensaje": "No fue posible importar el PDF."
                }

            movimientos = resultado.get(
                "movimientos",
                []
            )

            movimientos_normalizados = (
                NormalizadorMovimientoService.normalizar_lista(
                    movimientos
                )
            )

            resumen = MovimientoService.importar_movimientos(
                db=db,
                cuenta_id=cuenta_id,
                movimientos=movimientos_normalizados
            )

            return {

                "ok": True,

                "mensaje": "Importación finalizada correctamente.",

                "banco": resultado.get("banco"),

                "archivo": resultado.get("archivo"),

                "cantidad_movimientos": len(
                    movimientos_normalizados
                ),

                "total_creditos": resultado.get(
                    "total_creditos",
                    0
                ),

                "total_debitos": resultado.get(
                    "total_debitos",
                    0
                ),

                "importados": resumen.get(
                    "importados",
                    0
                ),

                "duplicados": resumen.get(
                    "duplicados",
                    0
                ),

                "total": resumen.get(
                    "total",
                    len(movimientos_normalizados)
                )

            }

        except Exception as e:

            return {

                "ok": False,

                "mensaje": str(e),

                "banco": None,

                "archivo": ruta_pdf,

                "cantidad_movimientos": 0,

                "total_creditos": 0,

                "total_debitos": 0,

                "importados": 0,

                "duplicados": 0,

                "total": 0

            }