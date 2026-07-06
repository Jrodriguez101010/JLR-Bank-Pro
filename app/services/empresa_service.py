from app.models.empresa import Empresa
from app.repositories.empresa_repository import EmpresaRepository


class EmpresaService:

    @staticmethod
    def obtener_todas(db):
        return EmpresaRepository.obtener_todas(db)

    @staticmethod
    def obtener_por_id(db, empresa_id):
        return EmpresaRepository.obtener_por_id(db, empresa_id)

    @staticmethod
    def buscar(db, texto):

        if texto is None:
            texto = ""

        texto = texto.strip()

        if texto == "":
            return EmpresaRepository.obtener_todas(db)

        return EmpresaRepository.buscar(db, texto)

    @staticmethod
    def crear_empresa(db, datos):

        empresa = Empresa(
            razon_social=datos["razon_social"],
            nombre_fantasia=datos["nombre_fantasia"],
            cuit=datos["cuit"],
            direccion=datos["direccion"],
            localidad=datos["localidad"],
            provincia=datos["provincia"],
            telefono=datos["telefono"],
            email=datos["email"],
            activa=datos["activa"]
        )

        return EmpresaRepository.crear(db, empresa)

    @staticmethod
    def actualizar_empresa(db, empresa, datos):

        empresa.razon_social = datos["razon_social"]
        empresa.nombre_fantasia = datos["nombre_fantasia"]
        empresa.cuit = datos["cuit"]
        empresa.direccion = datos["direccion"]
        empresa.localidad = datos["localidad"]
        empresa.provincia = datos["provincia"]
        empresa.telefono = datos["telefono"]
        empresa.email = datos["email"]
        empresa.activa = datos["activa"]

        return EmpresaRepository.actualizar(db, empresa)

    @staticmethod
    def eliminar_empresa(db, empresa):

        EmpresaRepository.eliminar(db, empresa)