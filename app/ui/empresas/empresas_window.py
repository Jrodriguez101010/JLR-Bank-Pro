import tkinter as tk
from tkinter import ttk


class EmpresasWindow:

    def __init__(self):

        self.ventana = tk.Toplevel()

        self.ventana.title("Empresas")
        self.ventana.geometry("1100x650")
        self.ventana.resizable(False, False)

        self.crear_interfaz()

    # =====================================================
    # INTERFAZ
    # =====================================================

    def crear_interfaz(self):

        # ---------------------------------------------
        # TITULO
        # ---------------------------------------------

        titulo = tk.Label(
            self.ventana,
            text="Administración de Empresas",
            font=("Arial", 22, "bold"),
            fg="#0d6efd"
        )

        titulo.pack(pady=15)

        # ---------------------------------------------
        # BUSCADOR
        # ---------------------------------------------

        frame_busqueda = tk.Frame(self.ventana)
        frame_busqueda.pack(fill="x", padx=20)

        tk.Label(
            frame_busqueda,
            text="Buscar:"
        ).pack(side="left")

        self.txt_buscar = tk.Entry(
            frame_busqueda,
            width=50
        )

        self.txt_buscar.pack(
            side="left",
            padx=10
        )

        tk.Button(
            frame_busqueda,
            text="Buscar",
            width=12,
            bg="#0d6efd",
            fg="white",
            command=self.buscar
        ).pack(side="left")

        # ---------------------------------------------
        # TABLA
        # ---------------------------------------------

        frame_tabla = tk.Frame(self.ventana)

        frame_tabla.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        columnas = (
            "id",
            "razon",
            "fantasia",
            "cuit",
            "telefono",
            "email"
        )

        self.tabla = ttk.Treeview(
            frame_tabla,
            columns=columnas,
            show="headings",
            height=18
        )

        self.tabla.heading("id", text="ID")
        self.tabla.heading("razon", text="Razón Social")
        self.tabla.heading("fantasia", text="Nombre Fantasía")
        self.tabla.heading("cuit", text="CUIT")
        self.tabla.heading("telefono", text="Teléfono")
        self.tabla.heading("email", text="Email")

        self.tabla.column("id", width=60, anchor="center")
        self.tabla.column("razon", width=260)
        self.tabla.column("fantasia", width=180)
        self.tabla.column("cuit", width=150)
        self.tabla.column("telefono", width=130)
        self.tabla.column("email", width=250)

        scrollbar = ttk.Scrollbar(
            frame_tabla,
            orient="vertical",
            command=self.tabla.yview
        )

        self.tabla.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabla.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # ---------------------------------------------
        # BOTONES
        # ---------------------------------------------

        frame_botones = tk.Frame(self.ventana)

        frame_botones.pack(
            pady=10
        )

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
            text="Modificar",
            width=15,
            bg="#ffc107",
            command=self.modificar
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            frame_botones,
            text="Eliminar",
            width=15,
            bg="#dc3545",
            fg="white",
            command=self.eliminar
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            frame_botones,
            text="Actualizar",
            width=15,
            command=self.cargar_empresas
        ).grid(row=0, column=3, padx=5)

        tk.Button(
            frame_botones,
            text="Cerrar",
            width=15,
            command=self.ventana.destroy
        ).grid(row=0, column=4, padx=5)

        self.cargar_empresas()

    # =====================================================
    # METODOS
    # =====================================================

    def cargar_empresas(self):

        self.tabla.delete(*self.tabla.get_children())

        #
        # En la siguiente entrega
        # cargaremos los datos desde SQLite.
        #

        datos_demo = [

            (1, "Tech SA", "Tech", "20123456789", "123456", "tech@empresa.com"),
            (2, "Banco Demo", "Banco", "20999888777", "444555", "info@banco.com"),
            (3, "Servicios SRL", "Servicios", "20333444555", "555666", "ventas@srl.com")

        ]

        for fila in datos_demo:
            self.tabla.insert("", "end", values=fila)

    def buscar(self):
        print("Buscar empresa")

    def nuevo(self):
        print("Nueva empresa")

    def modificar(self):
        print("Modificar empresa")

    def eliminar(self):
        print("Eliminar empresa")

    def ejecutar(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    EmpresasWindow().ejecutar()