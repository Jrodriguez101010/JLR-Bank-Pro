import tkinter as tk
from tkinter import ttk, messagebox

from app.core.database import SessionLocal
from app.services.usuario_service import UsuarioService
from app.ui.inicio.inicio_window import InicioWindow


class LoginWindow:

    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title("JLR Bank Pro")
        self.ventana.geometry("500x400")
        self.ventana.resizable(False, False)

        titulo = tk.Label(
            self.ventana,
            text="JLR BANK PRO",
            font=("Arial", 20, "bold")
        )
        titulo.pack(pady=20)

        subtitulo = tk.Label(
            self.ventana,
            text="Sistema de Gestión Bancaria",
            font=("Arial", 12)
        )
        subtitulo.pack(pady=5)

        ttk.Separator(self.ventana).pack(fill="x", padx=30, pady=20)

        tk.Label(self.ventana, text="Usuario").pack()

        self.txt_usuario = tk.Entry(self.ventana, width=30)
        self.txt_usuario.pack(pady=5)

        tk.Label(self.ventana, text="Contraseña").pack()

        self.txt_password = tk.Entry(self.ventana, show="*", width=30)
        self.txt_password.pack(pady=5)

        tk.Button(
            self.ventana,
            text="Ingresar",
            width=20,
            bg="#0d6efd",
            fg="white",
            command=self.ingresar
        ).pack(pady=20)

        tk.Button(
            self.ventana,
            text="Salir",
            width=20,
            command=self.ventana.destroy
        ).pack()

    def ingresar(self):

        usuario = self.txt_usuario.get()
        password = self.txt_password.get()

        db = SessionLocal()

        try:

            user = UsuarioService.validar_login(
                db,
                usuario,
                password
            )

            if user:

                self.ventana.destroy()

                InicioWindow().ejecutar()

            else:

                messagebox.showerror(
                    "Error",
                    "Usuario o contraseña incorrectos."
                )

        finally:
            db.close()

    def ejecutar(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    LoginWindow().ejecutar()