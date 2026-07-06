import tkinter as tk
from tkinter import ttk, messagebox

from app.core.database import SessionLocal
from app.services.cliente_service import ClienteService


class ClienteForm:

    def __init__(self, parent):

        self.db = SessionLocal()

        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Cliente")
        self.ventana.geometry("650x600")
        self.ventana.resizable(False, False)

        titulo = tk.Label(
            self.ventana,
            text="Nuevo Cliente",
            font=("Arial", 18, "bold"),
            fg="#0d6efd"
        )

        titulo.pack(pady=15)

        frame = tk.Frame(self.ventana)
        frame.pack(fill="both", expand=True, padx=20)

        self.entries = {}

        campos = [
            ("Apellido", "apellido"),
            ("Nombre", "nombre"),
            ("DNI", "dni"),
            ("CUIT", "cuit"),
            ("Teléfono", "telefono"),
            ("Email", "email"),
            ("Domicilio", "domicilio"),
            ("Ciudad", "ciudad"),
            ("Provincia", "provincia"),
            ("Código Postal", "codigo_postal")
        ]

        for fila, (texto, clave) in enumerate(campos):

            tk.Label(
                frame,
                text=texto
            ).grid(row=fila, column=0, sticky="w", pady=5)

            entry = tk.Entry(frame, width=45)

            entry.grid(
                row=fila,
                column=1,
                pady=5
            )

            self.entries[clave] = entry

        frame_botones = tk.Frame(self.ventana)

        frame_botones.pack(pady=20)

        tk.Button(
            frame_botones,
            text="Guardar",
            width=15,
            bg="#198754",
            fg="white",
            command=self.guardar
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            frame_botones,
            text="Cancelar",
            width=15,
            command=self.cerrar
        ).grid(row=0, column=1, padx=10)

    def guardar(self):

        if not self.entries["apellido"].get().strip():
            messagebox.showwarning(
                "Atención",
                "Debe ingresar el apellido."
            )
            return

        if not self.entries["nombre"].get().strip():
            messagebox.showwarning(
                "Atención",
                "Debe ingresar el nombre."
            )
            return

        if not self.entries["dni"].get().strip():
            messagebox.showwarning(
                "Atención",
                "Debe ingresar el DNI."
            )
            return

        datos = {}

        for clave, entry in self.entries.items():
            datos[clave] = entry.get()

        ClienteService.crear(self.db, datos)

        messagebox.showinfo(
            "Clientes",
            "Cliente guardado correctamente."
        )

        self.cerrar()

    def cerrar(self):
        self.db.close()
        self.ventana.destroy()