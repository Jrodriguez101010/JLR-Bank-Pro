from app.models.cuenta_bancaria import CuentaBancaria
from app.repositories.cuenta_repository import CuentaRepository


class CuentaService:

    @staticmethod
    def listar(db):
        return CuentaRepository.listar(db)

    @staticmethod
    def listar_por_cliente(db, cliente_id):
        return CuentaRepository.listar_por_cliente(db, cliente_id)

    @staticmethod
    def buscar(db, texto):
        return CuentaRepository.buscar(db, texto)

    @staticmethod
    def crear(db, datos):

        cuenta = CuentaBancaria(
            cliente_id=datos["cliente_id"],
            banco=datos["banco"],
            sucursal=datos.get("sucursal"),
            tipo_cuenta=datos.get("tipo_cuenta"),
            numero_cuenta=datos.get("numero_cuenta"),
            cbu=datos.get("cbu"),
            alias=datos.get("alias"),
            moneda=datos.get("moneda", "ARS"),
            saldo_inicial=datos.get("saldo_inicial", 0),
            activa=True
        )

        return CuentaRepository.crear(db, cuenta)

    @staticmethod
    def actualizar(db, cuenta_id, datos):

        cuenta = CuentaRepository.obtener_por_id(db, cuenta_id)

        if not cuenta:
            raise ValueError("La cuenta bancaria no existe.")

        cuenta.cliente_id = datos["cliente_id"]
        cuenta.banco = datos["banco"]
        cuenta.sucursal = datos.get("sucursal")
        cuenta.tipo_cuenta = datos.get("tipo_cuenta")
        cuenta.numero_cuenta = datos.get("numero_cuenta")
        cuenta.cbu = datos.get("cbu")
        cuenta.alias = datos.get("alias")
        cuenta.moneda = datos.get("moneda", "ARS")
        cuenta.saldo_inicial = datos.get("saldo_inicial", 0)

        return CuentaRepository.actualizar(db, cuenta)

    @staticmethod
    def eliminar(db, cuenta_id):

        cuenta = CuentaRepository.obtener_por_id(db, cuenta_id)

        if not cuenta:
            raise ValueError("La cuenta bancaria no existe.")

        return CuentaRepository.desactivar(db, cuenta)