from typing import Optional


class ClasificadorService:
    """
    Motor de clasificación de movimientos.

    Las reglas se evalúan en orden.
    La primera coincidencia determina la clasificación.
    """

    REGLAS = [

        ("SIRCREB", [
            "SIRCREB",
            "SIR CREB"
        ]),

        ("INGRESOS BRUTOS", [
            "INGRESOS BRUTOS",
            "IIBB",
            "ARBA",
            "API",
            "DGR",
            "R.G. INGRESOS BRUTOS"
        ]),

        ("IMP. LEY 25.453", [
            "25.453",
            "LEY 25453",
            "IMPUESTO LEY"
        ]),

        ("IVA", [
            "IVA",
            "I.V.A."
        ]),

        ("GASTOS BANCARIOS", [
            "COMISION",
            "COMISIÓN",
            "MANTENIMIENTO",
            "SELLADO",
            "GASTO",
            "GASTOS",
            "IVA SERVICIOS"
        ]),

        ("DEP. TRANSF.", [
            "TRANSFERENCIA",
            "TRANSFER",
            "ACREDITACION",
            "ACREDITACIÓN",
            "DEPOSITO",
            "DEPÓSITO",
            "DEPOSITO EN EFECTIVO",
            "DEP. EFECTIVO",
            "ACRED.",
            "TRANSFERENCIA DE TERCEROS"
        ]),

        ("PAGOS Y EXTRAC.", [
            "PAGO",
            "EXTRACCION",
            "EXTRACCIÓN",
            "DEBITO",
            "DÉBITO",
            "CHEQUE",
            "TRANSFERENCIA ENVIADA",
            "TRANSFERENCIA REALIZADA",
            "PAGO MIS CUENTAS"
        ])

    ]

    @classmethod
    def normalizar(cls, texto: Optional[str]) -> str:

        if texto is None:
            return ""

        return (
            texto.upper()
                .strip()
                .replace("Á", "A")
                .replace("É", "E")
                .replace("Í", "I")
                .replace("Ó", "O")
                .replace("Ú", "U")
        )

    @classmethod
    def clasificar(cls, descripcion: Optional[str]) -> str:

        texto = cls.normalizar(descripcion)

        if texto == "":
            return "NETO"

        for categoria, palabras in cls.REGLAS:

            for palabra in palabras:

                if cls.normalizar(palabra) in texto:
                    return categoria

        return "NETO"

    @classmethod
    def agregar_regla(cls, categoria, palabras):

        cls.REGLAS.append(
            (
                categoria,
                palabras
            )
        )

    @classmethod
    def eliminar_regla(cls, categoria):

        cls.REGLAS = [
            r for r in cls.REGLAS
            if r[0] != categoria
        ]

    @classmethod
    def obtener_reglas(cls):

        return cls.REGLAS

    @classmethod
    def categorias(cls):

        return [
            categoria
            for categoria, _ in cls.REGLAS
        ]