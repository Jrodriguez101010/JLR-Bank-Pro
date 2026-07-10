class DetectorBanco:

    @staticmethod
    def detectar(texto):

        texto = texto.upper()

        # ---------- GALICIA ----------
        if (
            "BANCO GALICIA" in texto
            or "GALICIA" in texto
            or "RESUMEN DE CUENTA CORRIENTE EN PESOS" in texto
            or "N° 000" in texto
            or "CUENTA CORRIENTE EN PESOS" in texto
        ):
            return "GALICIA"

        # ---------- SANTANDER ----------
        if (
            "BANCO SANTANDER" in texto
            or "SANTANDER" in texto
        ):
            return "SANTANDER"

        # ---------- BBVA ----------
        if (
            "BBVA" in texto
            or "BANCO BBVA" in texto
            or "BBVA ARGENTINA" in texto
        ):
            return "BBVA"

        # ---------- MACRO ----------
        if (
            "BANCO MACRO" in texto
            or "MACRO" in texto
        ):
            return "MACRO"

        # ---------- NACION ----------
        if (
            "BANCO DE LA NACION ARGENTINA" in texto
            or "BANCO DE LA NACIÓN ARGENTINA" in texto
            or "BANCO NACION" in texto
        ):
            return "NACION"

        return "DESCONOCIDO"