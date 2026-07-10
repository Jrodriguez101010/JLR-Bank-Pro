import tkinter as tk
from tkinter import ttk, messagebox

from app.core.database import SessionLocal
from app.services.cuenta_service import CuentaService
from app.ui.cuentas.cuenta_form import CuentaForm


class CuentasWindow:

    def __init__(self, parent=None):

        self.db = SessionLocal()

        self.ventana = tk.Toplevel(parent) if parent else tk.Tk()

        self.ventana.title("Cuentas Bancarias")
        self.ventana.geometry("1250x650")
        self.ventana.resizable(False, False)

        self.crear_interfaz()

        self.cargar_cuentas()

    def crear_interfaz(self):

        tk.Label(
            self.ventana,
            text="Administración de Cuentas Bancarias",
            font=("Arial", 22, "bold"),
            fg="#0d6efd"
        ).pack(pady=15)

        frame_busqueda = tk.Frame(self.ventana)
        frame_busqueda.pack(fill="x", padx=20)

        tk.Label(frame_busqueda, text="Buscar").pack(side="left")

        self.txt_buscar = tk.Entry(frame_busqueda, width=45)
        self.txt_buscar.pack(side="left", padx=10)

        self.txt_buscar.bind(
            "<KeyRelease>",
            lambda e: self.buscar()
        )

        columnas = (
            "id",
            "cliente",
            "banco",
            "tipo",
            "numero",
            "cbu",
            "alias",
            "moneda"
        )

        self.tabla = ttk.Treeview(
            self.ventana,
            columns=columnas,
            show="headings",
            height=18
        )

        encabezados = {
            "id": "ID",
            "cliente": "CLIENTE",
            "banco": "BANCO",
            "tipo": "TIPO",
            "numero": "NÚMERO",
            "cbu": "CBU",
            "alias": "ALIAS",
            "moneda": "MONEDA"
        }

        for c in columnas:
            self.tabla.heading(c, text=encabezados[c])

        self.tabla.column("id", width=60, anchor="center")
        self.tabla.column("cliente", width=220)
        self.tabla.column("banco", width=150)
        self.tabla.column("tipo", width=120)
        self.tabla.column("numero", width=150)
        self.tabla.column("cbu", width=180)
        self.tabla.column("alias", width=180)
        self.tabla.column("moneda", width=80, anchor="center")

        self.tabla.pack(fill="both", expand=True, padx=20, pady=20)

        self.tabla.bind(
            "<Double-1>",
            lambda e: self.editar()
        )

        botones = tk.Frame(self.ventana)
        botones.pack(pady=10)

        tk.Button(
            botones,
            text="Nueva",
            width=15,
            bg="#198754",
            fg="white",
            command=self.nueva
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            botones,
            text="Editar",
            width=15,
            command=self.editar
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            botones,
            text="Eliminar",
            width=15,
            bg="#dc3545",
            fg="white",
            command=self.eliminar
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            botones,
            text="Actualizar",
            width=15,
            command=self.cargar_cuentas
        ).grid(row=0, column=3, padx=5)

        tk.Button(
            botones,
            text="Cerrar",
            width=15,
            command=self.cerrar
        ).grid(row=0, column=4, padx=5)

    def cargar_cuentas(self):

        self.tabla.delete(*self.tabla.get_children())

        cuentas = CuentaService.listar(self.db)

        for c in cuentas:

            self.tabla.insert(
                "",
                "end",
                values=(
                    c.id,
                    f"{c.cliente.apellido}, {c.cliente.nombre}",
                    c.banco,
                    c.tipo_cuenta,
                    c.numero_cuenta,
                    c.cbu,
                    c.alias,
                    c.moneda
                )
            )

    def buscar(self):

        texto = self.txt_buscar.get().strip()

        self.tabla.delete(*self.tabla.get_children())

        if texto:
            cuentas = CuentaService.buscar(self.db, texto)
        else:
            cuentas = CuentaService.listar(self.db)

        for c in cuentas:

            self.tabla.insert(
                "",
                "end",
                values=(
                    c.id,
                    f"{c.cliente.apellido}, {c.cliente.nombre}",
                    c.banco,
                    c.tipo_cuenta,
                    c.numero_cuenta,
                    c.cbu,
                    c.alias,
                    c.moneda
                )
            )

    def obtener_id(self):

        seleccion = self.tabla.selection()

        if not seleccion:

            messagebox.showwarning(
                "Cuenta",
                "Seleccione una cuenta."
            )

            return None

        return int(
            self.tabla.item(
                seleccion[0]
            )["values"][0]
        )

    def nueva(self):

        formulario = CuentaForm(self.ventana)

        self.ventana.wait_window(
            formulario.ventana
        )

        self.cargar_cuentas()

    def editar(self):

        messagebox.showinfo(
            "Versión 0.3",
            "La edición se implementará en la siguiente entrega."
        )

    def eliminar(self):

        cuenta_id = self.obtener_id()

        if cuenta_id is None:
            return

        if not messagebox.askyesno(
            "Confirmar",
            "¿Desea desactivar esta cuenta?"
        ):
            return

        CuentaService.eliminar(
            self.db,
            cuenta_id
        )

        self.cargar_cuentas()

    def cerrar(self):

        self.db.close()

        self.ventana.destroy()


if __name__ == "__main__":

    CuentasWindow().ventana.mainloop()