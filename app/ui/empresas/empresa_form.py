import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class EmpresaForm:

    def __init__(self, parent):

        self.parent = parent

        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Empresa")
        self.ventana.geometry("650x620")
        self.ventana.resizable(False, False)

        titulo = tk.Label(
            self.ventana,
            text="Formulario de Empresa",
            font=("Arial", 18, "bold"),
            fg="#0d6efd"
        )

        titulo.pack(pady=15)

        frame = tk.Frame(self.ventana)

        frame.pack(fill="both", expand=True, padx=20)

        # -------------------------
        # RAZON SOCIAL
        # -------------------------

        tk.Label(
            frame,
            text="Razón Social"
        ).grid(row=0, column=0, sticky="w", pady=5)

        self.txt_razon = tk.Entry(
            frame,
            width=45
        )

        self.txt_razon.grid(
            row=0,
            column=1,
            pady=5
        )

        # -------------------------
        # NOMBRE FANTASIA
        # -------------------------

        tk.Label(
            frame,
            text="Nombre Fantasía"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            pady=5
        )

        self.txt_fantasia = tk.Entry(
            frame,
            width=45
        )

        self.txt_fantasia.grid(
            row=1,
            column=1,
            pady=5
        )

        # -------------------------
        # CUIT
        # -------------------------

        tk.Label(
            frame,
            text="CUIT"
        ).grid(
            row=2,
            column=0,
            sticky="w",
            pady=5
        )

        self.txt_cuit = tk.Entry(
            frame,
            width=45
        )

        self.txt_cuit.grid(
            row=2,
            column=1,
            pady=5
        )

        # -------------------------
        # DIRECCION
        # -------------------------

        tk.Label(
            frame,
            text="Dirección"
        ).grid(
            row=3,
            column=0,
            sticky="w",
            pady=5
        )

        self.txt_direccion = tk.Entry(
            frame,
            width=45
        )

        self.txt_direccion.grid(
            row=3,
            column=1,
            pady=5
        )

        # -------------------------
        # LOCALIDAD
        # -------------------------

        tk.Label(
            frame,
            text="Localidad"
        ).grid(
            row=4,
            column=0,
            sticky="w",
            pady=5
        )

        self.txt_localidad = tk.Entry(
            frame,
            width=45
        )

        self.txt_localidad.grid(
            row=4,
            column=1,
            pady=5
        )
        self.txt_localidad.grid(
    row=4,
    column=1,
    pady=5
)
        # -------------------------
        # PROVINCIA
        # -------------------------

        tk.Label(
            frame,
            text="Provincia"
        ).grid(
            row=5,
            column=0,
            sticky="w",
            pady=5
        )

        self.txt_provincia = tk.Entry(
            frame,
            width=45
        )

        self.txt_provincia.grid(
            row=5,
            column=1,
            pady=5
        )

        # -------------------------
        # TELEFONO
        # -------------------------

        tk.Label(
            frame,
            text="Teléfono"
        ).grid(
            row=6,
            column=0,
            sticky="w",
            pady=5
        )

        self.txt_telefono = tk.Entry(
            frame,
            width=45
        )

        self.txt_telefono.grid(
            row=6,
            column=1,
            pady=5
        )

        # -------------------------
        # EMAIL
        # -------------------------

        tk.Label(
            frame,
            text="Email"
        ).grid(
            row=7,
            column=0,
            sticky="w",
            pady=5
        )

        self.txt_email = tk.Entry(
            frame,
            width=45
        )

        self.txt_email.grid(
            row=7,
            column=1,
            pady=5
        )

        # -------------------------
        # ACTIVO
        # -------------------------

        tk.Label(
            frame,
            text="Activo"
        ).grid(
            row=8,
            column=0,
            sticky="w",
            pady=5
        )

        self.cbo_activo = ttk.Combobox(
            frame,
            values=["Sí", "No"],
            state="readonly",
            width=42
        )

        self.cbo_activo.current(0)

        self.cbo_activo.grid(
            row=8,
            column=1,
            pady=5
        )

        # -------------------------
        # BOTONES
        # -------------------------

        frame_botones = tk.Frame(self.ventana)

        frame_botones.pack(pady=25)

        tk.Button(
            frame_botones,
            text="Guardar",
            bg="#0d6efd",
            fg="white",
            width=15,
            command=self.guardar
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            frame_botones,
            text="Cancelar",
            width=15,
            command=self.ventana.destroy
        ).grid(row=0, column=1, padx=10)
    def guardar(self):

        if self.txt_razon.get().strip() == "":
            messagebox.showwarning(
                "Atención",
                "Debe ingresar la Razón Social."
            )
            return

        if self.txt_cuit.get().strip() == "":
            messagebox.showwarning(
                "Atención",
                "Debe ingresar el CUIT."
            )
            return

        datos = {
            "razon_social": self.txt_razon.get(),
            "nombre_fantasia": self.txt_fantasia.get(),
            "cuit": self.txt_cuit.get(),
            "direccion": self.txt_direccion.get(),
            "localidad": self.txt_localidad.get(),
            "provincia": self.txt_provincia.get(),
            "telefono": self.txt_telefono.get(),
            "email": self.txt_email.get(),
            "activo": 1 if self.cbo_activo.get() == "Sí" else 0
        }

        print(datos)

        messagebox.showinfo(
            "Empresa",
            "Formulario terminado.\n\nEn la próxima entrega guardaremos estos datos en la base de datos."
        )

        self.ventana.destroy()


    def ejecutar(self):
        self.ventana.grab_set()
        self.ventana.focus()
        self.ventana.wait_window()


if __name__ == "__main__":

    raiz = tk.Tk()
    raiz.withdraw()

    EmpresaForm(raiz).ejecutar()                