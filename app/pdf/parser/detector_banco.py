class DetectorBanco:

    @staticmethod
    def detectar(texto):

        texto = texto.upper()

        bancos = {

            "GALICIA": [
                "BANCO GALICIA",
                "GALICIA",
                "RESUMEN DE CUENTA CORRIENTE",
                "CUENTA CORRIENTE EN PESOS",
                "BANCO DE GALICIA"
            ],

            "SANTANDER": [
                "BANCO SANTANDER",
                "SANTANDER RIO",
                "SANTANDER"
            ],

            "BBVA": [
                "BBVA",
                "BANCO BBVA",
                "BBVA ARGENTINA",
                "BANCO FRANCES"
            ],

            "MACRO": [
                "BANCO MACRO",
                "MACRO"
            ],

            "CREDICOOP": [
                "CREDICOOP",
                "BANCO CREDICOOP"
            ],

            "NACION": [
                "BANCO DE LA NACION ARGENTINA",
                "BANCO DE LA NACIÓN ARGENTINA",
                "BANCO NACION",
                "BNA"
            ]
        }

        for banco, palabras in bancos.items():

            for palabra in palabras:

                if palabra in texto:
                    return banco

        return "DESCONOCIDO"