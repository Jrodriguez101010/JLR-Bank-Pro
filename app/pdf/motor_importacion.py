from app.pdf.pdf_reader import PDFReader
from app.pdf.parser.detector_banco import DetectorBanco
from app.pdf.parser.galicia import ParserGalicia


class MotorImportacion:

    @staticmethod
    def importar(ruta_pdf):

        # Leer PDF
        texto = PDFReader.extraer_texto(ruta_pdf)

        # Detectar banco
        banco = DetectorBanco.detectar(texto)

        # Elegir parser
        if banco == "GALICIA":
            movimientos = ParserGalicia.extraer_movimientos(texto)
        else:
            movimientos = []

        return {
            "banco": banco,
            "movimientos": movimientos
        }