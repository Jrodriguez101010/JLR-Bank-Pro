from app.models.cliente import Cliente
from app.repositories.cliente_repository import ClienteRepository


class ClienteService:

    @staticmethod
    def listar(db):
        return ClienteRepository.listar_activos(db)

    @staticmethod
    def buscar(db, texto):
        return ClienteRepository.buscar(db, texto)

    @staticmethod
    def obtener_por_id(db, cliente_id):
        return ClienteRepository.obtener_por_id(db, cliente_id)

    @staticmethod
    def crear(db, datos):

        existente = ClienteRepository.obtener_por_dni(
            db,
            datos["dni"]
        )

        if existente:
            raise ValueError("Ya existe un cliente con ese DNI.")

        cliente = Cliente(
            apellido=datos["apellido"],
            nombre=datos["nombre"],
            dni=datos["dni"],
            cuit=datos.get("cuit", ""),
            telefono=datos.get("telefono", ""),
            email=datos.get("email", ""),
            domicilio=datos.get("domicilio", ""),
            ciudad=datos.get("ciudad", ""),
            provincia=datos.get("provincia", ""),
            codigo_postal=datos.get("codigo_postal", ""),
            activo=True
        )

        return ClienteRepository.crear(db, cliente)

    @staticmethod
    def actualizar(db, cliente_id, datos):

        cliente = ClienteRepository.obtener_por_id(
            db,
            cliente_id
        )

        if cliente is None:
            raise ValueError("Cliente no encontrado.")

        otro = ClienteRepository.obtener_por_dni(
            db,
            datos["dni"]
        )

        if otro and otro.id != cliente.id:
            raise ValueError("Ya existe otro cliente con ese DNI.")

        cliente.apellido = datos["apellido"]
        cliente.nombre = datos["nombre"]
        cliente.dni = datos["dni"]
        cliente.cuit = datos.get("cuit", "")
        cliente.telefono = datos.get("telefono", "")
        cliente.email = datos.get("email", "")
        cliente.domicilio = datos.get("domicilio", "")
        cliente.ciudad = datos.get("ciudad", "")
        cliente.provincia = datos.get("provincia", "")
        cliente.codigo_postal = datos.get("codigo_postal", "")

        return ClienteRepository.actualizar(db, cliente)

    @staticmethod
    def eliminar(db, cliente_id):

        cliente = ClienteRepository.obtener_por_id(
            db,
            cliente_id
        )

        if cliente is None:
            raise ValueError("Cliente no encontrado.")

        return ClienteRepository.desactivar(
            db,
            cliente
        )