from app.core.database import SessionLocal, Base, engine

from app.models.empresa import Empresa
from app.models.usuario import Usuario

from app.services.empresa_service import EmpresaService
from app.services.usuario_service import UsuarioService

# Crear tablas
Base.metadata.create_all(bind=engine)


def main():
    db = SessionLocal()

    try:
        print("🚀 PROBANDO SISTEMA")

        # EMPRESA
        empresa = EmpresaService.crear_empresa(db, {
            "razon_social": "Tech SA",
            "nombre_fantasia": "Tech",
            "cuit": "20123456789",
            "direccion": "Buenos Aires",
            "localidad": "CABA",
            "provincia": "Buenos Aires",
            "telefono": "123456",
            "email": "tech@empresa.com",
            "activa": True
        })

        print("✅ Empresa creada:", empresa.id)

        # USUARIO
        usuario = UsuarioService.crear_usuario(db, {
            "nombre": "José",
            "apellido": "Rodríguez",
            "usuario": "jrodriguez",
            "password": "123456",
            "email": "jose@test.com",
            "rol": "Administrador",
            "activo": True
        })

        print("✅ Usuario creado:", usuario.id)

    finally:
        db.close()


if __name__ == "__main__":
    main()