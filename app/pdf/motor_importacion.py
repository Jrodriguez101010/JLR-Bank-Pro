from app.pdf.pdf_reader import PDFReader
from app.pdf.parser.detector_banco import DetectorBanco
from app.pdf.parser.galicia import ParserGalicia


class MotorImportacion:

    PARSERS = {
        "GALICIA": ParserGalicia,
    }

    @classmethod
    def importar(cls, ruta_pdf):

        texto = PDFReader.extraer_texto(ruta_pdf)

        banco = DetectorBanco.detectar(texto)

        if banco == "DESCONOCIDO":
            raise Exception("No fue posible identificar el banco del PDF.")

        if banco not in cls.PARSERS:
            raise Exception(f"Parser no implementado para {banco}")

        parser = cls.PARSERS[banco]

        movimientos = parser.extraer_movimientos(texto)

        return cls._normalizar_resultado(
            banco=banco,
            ruta_pdf=ruta_pdf,
            movimientos=movimientos
        )

    @staticmethod
    def _normalizar_resultado(banco, ruta_pdf, movimientos):

        total_creditos = 0.0
        total_debitos = 0.0

        for mov in movimientos:

            total_creditos += mov.get("credito", 0)

            total_debitos += mov.get("debito", 0)

        return {

            "banco": banco,

            "archivo": ruta_pdf,

            "cantidad_movimientos": len(movimientos),

            "total_creditos": round(total_creditos, 2),

            "total_debitos": round(total_debitos, 2),

            "movimientos": movimientos

        }