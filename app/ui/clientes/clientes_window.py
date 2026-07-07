import tkinter as tk
from tkinter import ttk, messagebox

from app.core.database import SessionLocal
from app.services.cliente_service import ClienteService
from app.ui.clientes.cliente_form import ClienteForm


class ClientesWindow:

    def __init__(self, parent=None):

        self.db = SessionLocal()

        self.ventana = tk.Toplevel(parent) if parent else tk.Tk()

        self.ventana.title("Administración de Clientes")
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

        self.txt_buscar.bind(
            "<KeyRelease>",
            lambda e: self.buscar()
        )

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
        self.tabla.column("telefono", width=140)
        self.tabla.column("email", width=260)

        self.tabla.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.tabla.bind(
            "<Double-1>",
            lambda e: self.editar()
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
            command=self.cargar_clientes
        ).grid(row=0, column=3, padx=5)

        tk.Button(
            botones,
            text="Cerrar",
            width=15,
            command=self.cerrar
        ).grid(row=0, column=4, padx=5)

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

        texto = self.txt_buscar.get().strip()

        self.tabla.delete(*self.tabla.get_children())

        if texto:
            clientes = ClienteService.buscar(self.db, texto)
        else:
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

    def obtener_id_seleccionado(self):

        seleccion = self.tabla.selection()

        if not seleccion:

            messagebox.showwarning(
                "Clientes",
                "Seleccione un cliente."
            )

            return None

        return int(
            self.tabla.item(
                seleccion[0]
            )["values"][0]
        )

    def nuevo(self):

        formulario = ClienteForm(self.ventana)

        self.ventana.wait_window(
            formulario.ventana
        )

        self.cargar_clientes()

    def editar(self):

        cliente_id = self.obtener_id_seleccionado()

        if cliente_id is None:
            return

        formulario = ClienteForm(
            self.ventana,
            cliente_id
        )

        self.ventana.wait_window(
            formulario.ventana
        )

        self.cargar_clientes()

    def eliminar(self):

        cliente_id = self.obtener_id_seleccionado()

        if cliente_id is None:
            return

        if not messagebox.askyesno(
            "Confirmar",
            "¿Desea desactivar este cliente?"
        ):
            return

        try:

            ClienteService.eliminar(
                self.db,
                cliente_id
            )

            self.cargar_clientes()

            messagebox.showinfo(
                "Clientes",
                "Cliente desactivado correctamente."
            )

        except ValueError as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def cerrar(self):

        self.db.close()

        self.ventana.destroy()


if __name__ == "__main__":

    ClientesWindow().ventana.mainloop()