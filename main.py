from app.core.database import Base, engine

# Importar todos los modelos para que SQLAlchemy cree las tablas
from app.models.empresa import Empresa
from app.models.usuario import Usuario
from app.models.cliente import Cliente

from app.ui.clientes.clientes_window import ClientesWindow


# Crear tablas si no existen
Base.metadata.create_all(bind=engine)


def main():
    print("===================================")
    print("      JLR BANK PRO - Versión 0.2")
    print("===================================")

    app = ClientesWindow()
    app.ventana.mainloop()


if __name__ == "__main__":
    main()