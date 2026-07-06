import tkinter as tk
from tkinter import ttk, messagebox

from app.core.database import SessionLocal
from app.services.cliente_service import ClienteService
from app.ui.clientes.cliente_form import ClienteForm


class ClientesWindow:

    def __init__(self, parent=None):

        self.db = SessionLocal()

        self.ventana = tk.Toplevel(parent) if parent else tk.Tk()

        self.ventana.title("Clientes")
        self.ventana.geometry("1100x650")
        self.ventana.resizable(False, False)

        self.crear_interfaz()

        self.cargar_clientes()

    def crear_interfaz(self):

        tk.Label(
            self.ventana,
            text="Administración de Clientes",
            font=("Arial", 22, "bold"),
            fg="#0d6efd"
        ).pack(pady=15)

        frame_busqueda = tk.Frame(self.ventana)
        frame_busqueda.pack(fill="x", padx=20)

        tk.Label(
            frame_busqueda,
            text="Buscar:"
        ).pack(side="left")

        self.txt_buscar = tk.Entry(
            frame_busqueda,
            width=45
        )

        self.txt_buscar.pack(
            side="left",
            padx=10
        )

        tk.Button(
            frame_busqueda,
            text="Buscar",
            command=self.buscar
        ).pack(side="left")

        columnas = (
            "id",
            "apellido",
            "nombre",
            "dni",
            "telefono",
            "email"
        )

        self.tabla = ttk.Treeview(
            self.ventana,
            columns=columnas,
            show="headings",
            height=18
        )

        for col in columnas:
            self.tabla.heading(col, text=col.upper())

        self.tabla.column("id", width=60, anchor="center")
        self.tabla.column("apellido", width=180)
        self.tabla.column("nombre", width=180)
        self.tabla.column("dni", width=120)
        self.tabla.column("telefono", width=120)
        self.tabla.column("email", width=260)

        self.tabla.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        frame_botones = tk.Frame(self.ventana)

        frame_botones.pack(pady=10)

        tk.Button(
            frame_botones,
            text="Nuevo",
            width=15,
            bg="#198754",
            fg="white",
            command=self.nuevo
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            frame_botones,
            text="Actualizar",
            width=15,
            command=self.cargar_clientes
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            frame_botones,
            text="Cerrar",
            width=15,
            command=self.cerrar
        ).grid(row=0, column=2, padx=5)

    def cargar_clientes(self):

        self.tabla.delete(*self.tabla.get_children())

        clientes = ClienteService.listar(self.db)

        for c in clientes:

            self.tabla.insert(
                "",
                "end",
                values=(
                    c.id,
                    c.apellido,
                    c.nombre,
                    c.dni,
                    c.telefono,
                    c.email
                )
            )

    def buscar(self):

        texto = self.txt_buscar.get()

        self.tabla.delete(*self.tabla.get_children())

        clientes = ClienteService.buscar(
            self.db,
            texto
        )

        for c in clientes:

            self.tabla.insert(
                "",
                "end",
                values=(
                    c.id,
                    c.apellido,
                    c.nombre,
                    c.dni,
                    c.telefono,
                    c.email
                )
            )

    def nuevo(self):

        ClienteForm(self.ventana)

        self.ventana.wait_window()

        self.cargar_clientes()

    def cerrar(self):

        self.db.close()

        self.ventana.destroy()


if __name__ == "__main__":

    ClientesWindow().ventana.mainloop()