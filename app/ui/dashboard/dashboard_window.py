import tkinter as tk


class DashboardWindow:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("JLR Bank Pro")
        self.root.geometry("1400x800")
        self.root.state("zoomed")

        self.crear_interfaz()

    def crear_interfaz(self):

        barra_superior = tk.Frame(
            self.root,
            bg="#0d6efd",
            height=60
        )

        barra_superior.pack(
            fill="x"
        )

        barra_superior.pack_propagate(False)

        tk.Label(
            barra_superior,
            text="JLR BANK PRO",
            bg="#0d6efd",
            fg="white",
            font=("Arial", 18, "bold")
        ).pack(
            side="left",
            padx=20
        )

        self.menu = tk.Frame(
            self.root,
            bg="#f4f4f4",
            width=240
        )

        self.menu.pack(
            side="left",
            fill="y"
        )

        self.menu.pack_propagate(False)

        self.contenido = tk.Frame(
            self.root,
            bg="white"
        )

        self.contenido.pack(
            side="right",
            expand=True,
            fill="both"
        )

        opciones = [
            "Dashboard",
            "Empresas",
            "Usuarios",
            "Clientes",
            "Cuentas Bancarias",
            "Importar PDF",
            "Movimientos",
            "Clasificación",
            "Reportes",
            "Configuración"
        ]

        for opcion in opciones:

            tk.Button(
                self.menu,
                text=opcion,
                width=24,
                height=2
            ).pack(
                pady=3,
                padx=10
            )

        self.lbl = tk.Label(
            self.contenido,
            text="Bienvenido a JLR Bank Pro",
            font=("Arial", 24, "bold")
        )

        self.lbl.pack(
            pady=40
        )

    def ejecutar(self):
        self.root.mainloop()


if __name__ == "__main__":
    DashboardWindow().ejecutar()