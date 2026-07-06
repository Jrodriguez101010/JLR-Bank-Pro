from sqlalchemy.orm import Session

from app.models.usuario import Usuario
from app.repositories.usuario_repository import UsuarioRepository


class UsuarioService:

    @staticmethod
    def listar_usuarios(db: Session):
        return UsuarioRepository.obtener_todos(db)

    @staticmethod
    def obtener_usuario(db: Session, usuario_id: int):
        return UsuarioRepository.obtener_por_id(db, usuario_id)

    @staticmethod
    def validar_login(db: Session, usuario: str, password: str):
        return UsuarioRepository.obtener_login(db, usuario, password)

    @staticmethod
    def crear_usuario(db: Session, data: dict):
        usuario = Usuario(**data)
        return UsuarioRepository.crear(db, usuario)