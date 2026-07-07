import tkinter as tk
from tkinter import messagebox

from app.core.database import SessionLocal
from app.services.cliente_service import ClienteService


class ClienteForm:

    def __init__(self, parent, cliente_id=None):

        self.db = SessionLocal()
        self.cliente_id = cliente_id

        self.ventana = tk.Toplevel(parent)
        self.ventana.geometry("650x600")
        self.ventana.resizable(False, False)

        if cliente_id:
            self.ventana.title("Editar Cliente")
            titulo = "Editar Cliente"
        else:
            self.ventana.title("Nuevo Cliente")
            titulo = "Nuevo Cliente"

        tk.Label(
            self.ventana,
            text=titulo,
            font=("Arial", 18, "bold"),
            fg="#0d6efd"
        ).pack(pady=15)

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

            tk.Label(frame, text=texto).grid(
                row=fila,
                column=0,
                sticky="w",
                pady=5
            )

            entry = tk.Entry(frame, width=45)

            entry.grid(
                row=fila,
                column=1,
                pady=5
            )

            self.entries[clave] = entry

        botones = tk.Frame(self.ventana)
        botones.pack(pady=20)

        tk.Button(
            botones,
            text="Guardar",
            width=15,
            bg="#198754",
            fg="white",
            command=self.guardar
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            botones,
            text="Cancelar",
            width=15,
            command=self.cerrar
        ).grid(row=0, column=1, padx=10)

        if self.cliente_id:
            self.cargar_cliente()

    def cargar_cliente(self):

        cliente = ClienteService.obtener_por_id(
            self.db,
            self.cliente_id
        )

        if not cliente:
            messagebox.showerror(
                "Error",
                "Cliente no encontrado."
            )
            self.cerrar()
            return

        self.entries["apellido"].insert(0, cliente.apellido)
        self.entries["nombre"].insert(0, cliente.nombre)
        self.entries["dni"].insert(0, cliente.dni)
        self.entries["cuit"].insert(0, cliente.cuit or "")
        self.entries["telefono"].insert(0, cliente.telefono or "")
        self.entries["email"].insert(0, cliente.email or "")
        self.entries["domicilio"].insert(0, cliente.domicilio or "")
        self.entries["ciudad"].insert(0, cliente.ciudad or "")
        self.entries["provincia"].insert(0, cliente.provincia or "")
        self.entries["codigo_postal"].insert(
            0,
            cliente.codigo_postal or ""
        )

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

        datos = {
            clave: entry.get().strip()
            for clave, entry in self.entries.items()
        }

        try:

            if self.cliente_id:

                ClienteService.actualizar(
                    self.db,
                    self.cliente_id,
                    datos
                )

                messagebox.showinfo(
                    "Clientes",
                    "Cliente actualizado correctamente."
                )

            else:

                ClienteService.crear(
                    self.db,
                    datos
                )

                messagebox.showinfo(
                    "Clientes",
                    "Cliente creado correctamente."
                )

            self.cerrar()

        except ValueError as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def cerrar(self):

        self.db.close()

        self.ventana.destroy()