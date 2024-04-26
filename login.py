import tkinter as tk
from tkinter import messagebox
from main_menu import MainMenu
from connection_db import Connection

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")

        # Variables de usuario y contraseña
        self.email_var = tk.StringVar()
        self.password_var = tk.StringVar()

        # Etiquetas y campos de entrada
        tk.Label(root, text="Usuario").grid(row=0, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(root, textvariable=self.email_var)
        self.email_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Contraseña").grid(row=1, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(root, show="*", textvariable=self.password_var)
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        # Botones de login y registro
        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=5)

    def login(self):
        # Obtener el usuario y la contraseña ingresados
        email = self.email_var.get()
        password = self.password_var.get()

        query = f"SELECT * from usuarios WHERE email = '{email}' AND password = '{password}' "

        with Connection.get_connection() as cn:
            with cn.cursor() as cursor: 
                try:
                    cursor.execute(query)
                    data = cursor.fetchall()
                except Exception as e:
                    messagebox.showerror(message=f'{e}')
                    print(e)
        
        if data == []:
            messagebox.showerror(message='Usuario o contraseña no validos: DataVacio')
        else:
            self.root.destroy()
            window = tk.Tk()
            self.main_menu = MainMenu(window, data[0][0], data[0][2])
            window.mainloop()                


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()
