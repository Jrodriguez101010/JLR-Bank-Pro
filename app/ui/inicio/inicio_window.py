import tkinter as tk
from tkinter import ttk


class InicioWindow:

    def __init__(self):

        self.ventana = tk.Tk()

        self.ventana.title("JLR BANK PRO - Inicio")
        self.ventana.geometry("1000x650")
        self.ventana.configure(bg="#F5F5F5")

        # =========================
        # ENCABEZADO
        # =========================

        encabezado = tk.Frame(self.ventana, bg="#0D6EFD", height=70)
        encabezado.pack(fill="x")

        titulo = tk.Label(
            encabezado,
            text="JLR BANK PRO",
            bg="#0D6EFD",
            fg="white",
            font=("Arial", 22, "bold")
        )
        titulo.pack(side="left", padx=20, pady=15)

        usuario = tk.Label(
            encabezado,
            text="Usuario: Administrador",
            bg="#0D6EFD",
            fg="white",
            font=("Arial", 12)
        )
        usuario.pack(side="right", padx=20)

        # =========================
        # MENÚ
        # =========================

        barra = tk.Menu(self.ventana)

        archivo = tk.Menu(barra, tearoff=0)
        archivo.add_command(label="Salir", command=self.ventana.destroy)
        barra.add_cascade(label="Archivo", menu=archivo)

        barra.add_command(label="Empresas")
        barra.add_command(label="Usuarios")
        barra.add_command(label="Clientes")
        barra.add_command(label="Cuentas")
        barra.add_command(label="Caja")
        barra.add_command(label="Préstamos")
        barra.add_command(label="Reportes")
        barra.add_command(label="Configuración")

        self.ventana.config(menu=barra)

        # =========================
        # CONTENIDO
        # =========================

        cuerpo = tk.Frame(self.ventana, bg="#F5F5F5")
        cuerpo.pack(fill="both", expand=True, pady=30)

        bienvenida = tk.Label(
            cuerpo,
            text="Bienvenido a JLR BANK PRO",
            bg="#F5F5F5",
            font=("Arial", 24, "bold")
        )
        bienvenida.pack(pady=20)

        subtitulo = tk.Label(
            cuerpo,
            text="Seleccione una opción para comenzar",
            bg="#F5F5F5",
            font=("Arial", 12)
        )
        subtitulo.pack()

        botones = tk.Frame(cuerpo, bg="#F5F5F5")
        botones.pack(pady=40)

        opciones = [
            "Empresas",
            "Usuarios",
            "Clientes",
            "Cuentas",
            "Caja",
            "Préstamos",
            "Reportes",
            "Configuración"
        ]

        fila = 0
        columna = 0

        for opcion in opciones:

            boton = tk.Button(
                botones,
                text=opcion,
                width=18,
                height=3,
                bg="#0D6EFD",
                fg="white",
                font=("Arial", 11, "bold")
            )

            boton.grid(row=fila, column=columna, padx=15, pady=15)

            columna += 1

            if columna == 2:
                columna = 0
                fila += 1

        # =========================
        # BARRA DE ESTADO
        # =========================

        estado = tk.Label(
            self.ventana,
            text="Sistema listo",
            relief="sunken",
            anchor="w"
        )

        estado.pack(fill="x", side="bottom")

    def ejecutar(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    InicioWindow().ejecutar()