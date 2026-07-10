import re


class ParserGalicia:

    @staticmethod
    def extraer_movimientos(texto):

        movimientos = []

        lineas = texto.split("\n")

        patron_fecha = re.compile(r"^\d{2}/\d{2}/\d{2}")

        i = 0

        while i < len(lineas):

            linea = lineas[i].strip()

            if patron_fecha.match(linea):

                movimiento = ParserGalicia._leer_movimiento(lineas, i)

                if movimiento:

                    movimientos.append(movimiento)

                i += 1
                continue

            i += 1

        return movimientos

    @staticmethod
    def _leer_movimiento(lineas, indice):

        linea = lineas[indice].strip()

        partes = linea.split()

        if len(partes) < 3:
            return None

        fecha = partes[0]

        descripcion = linea[len(fecha):].strip()

        credito = 0.0
        debito = 0.0
        saldo = 0.0

        numeros = re.findall(r"-?\d{1,3}(?:\.\d{3})*,\d{2}-?", linea)

        if len(numeros) == 2:

            importe = ParserGalicia._a_float(numeros[0])
            saldo = ParserGalicia._a_float(numeros[1])

            if importe >= 0:
                credito = importe
            else:
                debito = abs(importe)

        elif len(numeros) >= 3:

            credito = ParserGalicia._a_float(numeros[-3])
            debito = ParserGalicia._a_float(numeros[-2])
            saldo = ParserGalicia._a_float(numeros[-1])

        return {
            "fecha": fecha,
            "descripcion": descripcion,
            "credito": credito,
            "debito": debito,
            "saldo": saldo
        }

    @staticmethod
    def _a_float(valor):

        negativo = False

        valor = valor.strip()

        if valor.startswith("-"):
            negativo = True

        if valor.endswith("-"):
            negativo = True

        valor = valor.replace("-", "")
        valor = valor.replace(".", "")
        valor = valor.replace(",", ".")

        try:
            numero = float(valor)
        except:
            numero = 0.0

        if negativo:
            numero *= -1

        return numero