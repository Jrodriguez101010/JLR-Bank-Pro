from sqlalchemy import or_

from app.models.cliente import Cliente


class ClienteRepository:

    @staticmethod
    def listar(db):
        return (
            db.query(Cliente)
            .filter(Cliente.activo == True)
            .order_by(Cliente.apellido, Cliente.nombre)
            .all()
        )

    @staticmethod
    def listar_activos(db):
        return (
            db.query(Cliente)
            .filter(Cliente.activo == True)
            .order_by(Cliente.apellido, Cliente.nombre)
            .all()
        )

    @staticmethod
    def obtener_por_id(db, cliente_id):
        return (
            db.query(Cliente)
            .filter(Cliente.id == cliente_id)
            .first()
        )

    @staticmethod
    def obtener_por_dni(db, dni):
        return (
            db.query(Cliente)
            .filter(Cliente.dni == dni)
            .first()
        )

    @staticmethod
    def buscar(db, texto):

        texto = f"%{texto}%"

        return (
            db.query(Cliente)
            .filter(
                Cliente.activo == True,
                or_(
                    Cliente.apellido.like(texto),
                    Cliente.nombre.like(texto),
                    Cliente.dni.like(texto),
                    Cliente.cuit.like(texto)
                )
            )
            .order_by(Cliente.apellido)
            .all()
        )

    @staticmethod
    def crear(db, cliente):

        db.add(cliente)
        db.commit()
        db.refresh(cliente)

        return cliente

    @staticmethod
    def actualizar(db, cliente):

        db.commit()
        db.refresh(cliente)

        return cliente

    @staticmethod
    def desactivar(db, cliente):

        cliente.activo = False

        db.commit()

        return cliente