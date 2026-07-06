from app.models.cliente import Cliente
from app.repositories.cliente_repository import ClienteRepository


class ClienteService:

    @staticmethod
    def listar(db):
        return ClienteRepository.listar(db)

    @staticmethod
    def buscar(db, texto):
        return ClienteRepository.buscar(db, texto)

    @staticmethod
    def crear(db, datos):

        cliente = Cliente(
            apellido=datos["apellido"],
            nombre=datos["nombre"],
            dni=datos["dni"],
            cuit=datos.get("cuit"),
            telefono=datos.get("telefono"),
            email=datos.get("email"),
            domicilio=datos.get("domicilio"),
            ciudad=datos.get("ciudad"),
            provincia=datos.get("provincia"),
            codigo_postal=datos.get("codigo_postal"),
            estado=datos.get("estado", "ACTIVO")
        )

        return ClienteRepository.crear(db, cliente)

    @staticmethod
    def eliminar(db, cliente_id):

        cliente = ClienteRepository.obtener_por_id(
            db,
            cliente_id
        )

        if cliente:
            ClienteRepository.eliminar(
                db,
                cliente
            )