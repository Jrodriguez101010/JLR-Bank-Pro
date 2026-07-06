from sqlalchemy.orm import Session

from app.models.usuario import Usuario


class UsuarioRepository:

    @staticmethod
    def obtener_todos(db: Session):
        return db.query(Usuario).all()

    @staticmethod
    def obtener_por_id(db: Session, usuario_id: int):
        return db.query(Usuario).filter(
            Usuario.id == usuario_id
        ).first()

    @staticmethod
    def obtener_login(db: Session, usuario: str, password: str):
        return db.query(Usuario).filter(
            Usuario.usuario == usuario,
            Usuario.password == password,
            Usuario.activo == True
        ).first()

    @staticmethod
    def crear(db: Session, usuario: Usuario):
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario