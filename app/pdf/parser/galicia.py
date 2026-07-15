import re


class ParserGalicia:

    PATRON_FECHA = re.compile(r"^\d{2}/\d{2}/\d{2}")
    PATRON_NUMERO = re.compile(r"-?\d{1,3}(?:\.\d{3})*,\d{2}-?")

    @classmethod
    def extraer_movimientos(cls, texto):

        movimientos = []
        lineas = [l.rstrip() for l in texto.splitlines()]

        i = 0

        while i < len(lineas):

            linea = lineas[i].strip()

            if not cls.PATRON_FECHA.match(linea):
                i += 1
                continue

            bloque = [linea]

            j = i + 1

            while j < len(lineas):

                siguiente = lineas[j].strip()

                if cls.PATRON_FECHA.match(siguiente):
                    break

                if siguiente:
                    bloque.append(siguiente)

                j += 1

            movimiento = cls._parsear_bloque(bloque)

            if movimiento:
                movimientos.append(movimiento)

            i = j

        return movimientos

    @classmethod
    def _parsear_bloque(cls, bloque):

        texto = " ".join(bloque)

        partes = texto.split()

        if len(partes) < 2:
            return None

        fecha = partes[0]

        numeros = cls.PATRON_NUMERO.findall(texto)

        if len(numeros) < 2:
            return None

        saldo = cls._a_float(numeros[-1])

        credito = 0.0
        debito = 0.0

        if len(numeros) == 2:

            importe = cls._a_float(numeros[0])

            if importe >= 0:
                credito = importe
            else:
                debito = abs(importe)

        else:

            credito = cls._a_float(numeros[-3])
            debito = cls._a_float(numeros[-2])

        descripcion = texto[len(fecha):]

        for numero in numeros:
            descripcion = descripcion.replace(numero, "")

        descripcion = " ".join(descripcion.split())

        return {
            "fecha": fecha,
            "descripcion": descripcion,
            "credito": credito,
            "debito": debito,
            "saldo": saldo
        }

    @staticmethod
    def _a_float(valor):

        negativo = valor.startswith("-") or valor.endswith("-")

        valor = valor.replace("-", "")
        valor = valor.replace(".", "")
        valor = valor.replace(",", ".")

        try:
            numero = float(valor)
        except ValueError:
            numero = 0.0

        if negativo:
            numero *= -1

        return numero