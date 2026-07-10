import tkinter as tk
from tkinter import ttk, messagebox

from app.core.database import SessionLocal
from app.services.cliente_service import ClienteService
from app.services.cuenta_service import CuentaService


class CuentaForm:

    def __init__(self, parent, cuenta_id=None):

        self.db = SessionLocal()
        self.cuenta_id = cuenta_id

        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Cuenta Bancaria")
        self.ventana.geometry("620x520")
        self.ventana.resizable(False, False)

        tk.Label(
            self.ventana,
            text="Cuenta Bancaria",
            font=("Arial", 18, "bold"),
            fg="#0d6efd"
        ).pack(pady=15)

        frame = tk.Frame(self.ventana)
        frame.pack(padx=20, fill="both")

        fila = 0

        tk.Label(frame, text="Cliente").grid(row=fila, column=0, sticky="w", pady=5)

        self.cbo_cliente = ttk.Combobox(frame, width=45, state="readonly")
        self.cbo_cliente.grid(row=fila, column=1, pady=5)

        self.clientes = ClienteService.listar(self.db)
        self.cbo_cliente["values"] = [
            f"{c.id} - {c.apellido}, {c.nombre}"
            for c in self.clientes
        ]

        fila += 1

        campos = [
            ("Banco", "banco"),
            ("Sucursal", "sucursal"),
            ("Tipo de Cuenta", "tipo_cuenta"),
            ("Número de Cuenta", "numero_cuenta"),
            ("CBU", "cbu"),
            ("Alias", "alias"),
            ("Moneda", "moneda"),
            ("Saldo Inicial", "saldo_inicial")
        ]

        self.entries = {}

        for texto, clave in campos:

            tk.Label(frame, text=texto).grid(
                row=fila,
                column=0,
                sticky="w",
                pady=5
            )

            entry = tk.Entry(frame, width=48)
            entry.grid(row=fila, column=1, pady=5)

            self.entries[clave] = entry

            fila += 1

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

    def guardar(self):

        if self.cbo_cliente.current() == -1:
            messagebox.showwarning(
                "Cuenta",
                "Debe seleccionar un cliente."
            )
            return

        cliente = self.clientes[self.cbo_cliente.current()]

        datos = {
            "cliente_id": cliente.id
        }

        for clave, entry in self.entries.items():
            datos[clave] = entry.get()

        try:

            CuentaService.crear(
                self.db,
                datos
            )

            messagebox.showinfo(
                "Cuenta",
                "Cuenta bancaria guardada correctamente."
            )

            self.cerrar()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def cerrar(self):
        self.db.close()
        self.ventana.destroy()