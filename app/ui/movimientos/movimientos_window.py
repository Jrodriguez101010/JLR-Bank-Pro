import tkinter as tk
from tkinter import ttk

from app.core.database import SessionLocal
from app.services.movimiento_service import MovimientoService
from app.ui.movimientos.movimiento_form import MovimientoForm


class MovimientosWindow:

    def __init__(self, parent=None):

        self.db = SessionLocal()

        self.ventana = tk.Toplevel(parent) if parent else tk.Tk()

        self.ventana.title("Movimientos Bancarios")
        self.ventana.geometry("1300x700")

        self.crear_interfaz()

        self.cargar_movimientos()

    def crear_interfaz(self):

        tk.Label(
            self.ventana,
            text="Administración de Movimientos Bancarios",
            font=("Arial", 20, "bold"),
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
            width=40
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
            "fecha",
            "descripcion",
            "importe",
            "saldo",
            "tipo",
            "clasificacion"
        )

        self.tabla = ttk.Treeview(
            self.ventana,
            columns=columnas,
            show="headings",
            height=20
        )

        for col in columnas:
            self.tabla.heading(col, text=col.upper())

        self.tabla.column("id", width=60)
        self.tabla.column("fecha", width=100)
        self.tabla.column("descripcion", width=420)
        self.tabla.column("importe", width=120)
        self.tabla.column("saldo", width=120)
        self.tabla.column("tipo", width=120)
        self.tabla.column("clasificacion", width=220)

        self.tabla.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        botones = tk.Frame(self.ventana)
        botones.pack(pady=10)

        tk.Button(
            botones,
            text="Nuevo",
            width=15,
            bg="#198754",
            fg="white",
            command=self.nuevo
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            botones,
            text="Actualizar",
            width=15,
            command=self.cargar_movimientos
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            botones,
            text="Cerrar",
            width=15,
            command=self.cerrar
        ).grid(row=0, column=2, padx=5)

    def cargar_movimientos(self):

        self.tabla.delete(*self.tabla.get_children())

        movimientos = MovimientoService.listar(self.db)

        for m in movimientos:

            self.tabla.insert(
                "",
                "end",
                values=(
                    m.id,
                    m.fecha,
                    m.descripcion,
                    m.importe,
                    m.saldo,
                    m.tipo,
                    m.clasificacion
                )
            )

    def buscar(self):

        texto = self.txt_buscar.get()

        self.tabla.delete(*self.tabla.get_children())

        movimientos = MovimientoService.buscar(
            self.db,
            texto
        )

        for m in movimientos:

            self.tabla.insert(
                "",
                "end",
                values=(
                    m.id,
                    m.fecha,
                    m.descripcion,
                    m.importe,
                    m.saldo,
                    m.tipo,
                    m.clasificacion
                )
            )

    def nuevo(self):

        MovimientoForm(self.ventana)

        self.ventana.wait_window()

        self.cargar_movimientos()

    def cerrar(self):

        self.db.close()

        self.ventana.destroy()


if __name__ == "__main__":

    MovimientosWindow().ventana.mainloop()