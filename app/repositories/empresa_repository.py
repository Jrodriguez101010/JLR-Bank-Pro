from sqlalchemy import or_

from app.models.empresa import Empresa


class EmpresaRepository:

    @staticmethod
    def obtener_todas(db):
        return (
            db.query(Empresa)
            .order_by(Empresa.razon_social)
            .all()
        )

    @staticmethod
    def obtener_por_id(db, empresa_id):
        return (
            db.query(Empresa)
            .filter(Empresa.id == empresa_id)
            .first()
        )

    @staticmethod
    def crear(db, empresa):
        db.add(empresa)
        db.commit()
        db.refresh(empresa)
        return empresa

    @staticmethod
    def actualizar(db, empresa):
        db.commit()
        db.refresh(empresa)
        return empresa

    @staticmethod
    def eliminar(db, empresa):
        db.delete(empresa)
        db.commit()

    @staticmethod
    def buscar(db, texto):
        return (
            db.query(Empresa)
            .filter(
                or_(
                    Empresa.razon_social.contains(texto),
                    Empresa.nombre_fantasia.contains(texto),
                    Empresa.cuit.contains(texto),
                )
            )
            .order_by(Empresa.razon_social)
            .all()
        )