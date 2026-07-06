from app.models.cliente import Cliente


class ClienteRepository:

    @staticmethod
    def listar(db):
        return db.query(Cliente).order_by(Cliente.apellido, Cliente.nombre).all()

    @staticmethod
    def obtener_por_id(db, cliente_id):
        return db.query(Cliente).filter(
            Cliente.id == cliente_id
        ).first()

    @staticmethod
    def obtener_por_dni(db, dni):
        return db.query(Cliente).filter(
            Cliente.dni == dni
        ).first()

    @staticmethod
    def buscar(db, texto):
        texto = f"%{texto}%"

        return db.query(Cliente).filter(
            (Cliente.apellido.like(texto)) |
            (Cliente.nombre.like(texto)) |
            (Cliente.dni.like(texto)) |
            (Cliente.cuit.like(texto))
        ).all()

    @staticmethod
    def crear(db, cliente):
        db.add(cliente)
        db.commit()
        db.refresh(cliente)
        return cliente

    @staticmethod
    def eliminar(db, cliente):
        db.delete(cliente)
        db.commit()