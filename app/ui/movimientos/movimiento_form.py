import tkinter as tk
from tkinter import messagebox
from datetime import datetime

from app.core.database import SessionLocal
from app.services.movimiento_service import MovimientoService


class MovimientoForm:

    def __init__(self, parent):

        self.db = SessionLocal()

        self.ventana = tk.Toplevel(parent)

        self.ventana.title("Movimiento Bancario")
        self.ventana.geometry("700x650")
        self.ventana.resizable(False, False)

        tk.Label(
            self.ventana,
            text="Nuevo Movimiento",
            font=("Arial", 18, "bold"),
            fg="#0d6efd"
        ).pack(pady=15)

        frame = tk.Frame(self.ventana)
        frame.pack(fill="both", expand=True, padx=20)

        self.entries = {}

        campos = [
            ("Cuenta ID", "cuenta_id"),
            ("Fecha (AAAA-MM-DD)", "fecha"),
            ("Descripción", "descripcion"),
            ("Importe", "importe"),
            ("Saldo", "saldo"),
            ("Tipo", "tipo"),
            ("Clasificación", "clasificacion"),
            ("Observaciones", "observaciones")
        ]

        for fila, (texto, clave) in enumerate(campos):

            tk.Label(
                frame,
                text=texto
            ).grid(row=fila, column=0, sticky="w", pady=6)

            entry = tk.Entry(frame, width=50)

            entry.grid(
                row=fila,
                column=1,
                pady=6
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

        try:

            datos = {
                "cuenta_id": int(self.entries["cuenta_id"].get()),
                "fecha": datetime.strptime(
                    self.entries["fecha"].get(),
                    "%Y-%m-%d"
                ).date(),
                "descripcion": self.entries["descripcion"].get(),
                "importe": float(self.entries["importe"].get()),
                "saldo": float(self.entries["saldo"].get() or 0),
                "tipo": self.entries["tipo"].get(),
                "clasificacion": self.entries["clasificacion"].get(),
                "observaciones": self.entries["observaciones"].get(),
                "procesado": False
            }

            MovimientoService.crear(
                self.db,
                datos
            )

            messagebox.showinfo(
                "Movimientos",
                "Movimiento guardado correctamente."
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