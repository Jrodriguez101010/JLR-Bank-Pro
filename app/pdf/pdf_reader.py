import pdfplumber


class PDFReader:

    @staticmethod
    def extraer_texto(ruta_pdf):

        texto = ""

        with pdfplumber.open(ruta_pdf) as pdf:

            for pagina in pdf.pages:

                contenido = pagina.extract_text()

                if contenido:
                    texto += contenido
                    texto += "\n"

        return texto