class TipoMovimientoService:

    @staticmethod
    def obtener_tipo(importe):

        if importe >= 0:
            return "CREDITO"

        return "DEBITO"

    @staticmethod
    def obtener_clasificacion_por_defecto(importe):

        if importe >= 0:
            return "DEP. TRANSF."

        return "PAGOS Y EXTRAC."