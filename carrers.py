import tkinter as tk
from tkinter import messagebox, ttk
from connection_db import Connection

class Carrers:
    def __init__(self, root, name):
        self.root = root
        self.root.title("Carreras")

        self.root.geometry("500x300")
        self.root.resizable(height=False, width=False)

        self.name = name
        tk.Label(self.root, text=f'¡USUARIO ACTUAL: {self.name}!', font='Arial 10').place(x=30, y=30)

        tk.Label(self.root, text='Ingresa codigo nombre: ').place(x=60, y=60)
        self.txt_clave_search = tk.Entry(self.root)
        self.txt_clave_search.place(x=210, y=60)

        tk.Label(self.root, text='Clave: ').place(x=20, y=100)
        self.txt_clave= tk.Entry(self.root, state=tk.DISABLED)
        self.txt_clave.place(x=120, y=100)
        
        tk.Label(self.root, text='Nombre: ').place(x=20, y=140)
        self.txt_nombre= tk.Entry(self.root, state=tk.DISABLED)
        self.txt_nombre.place(x=120, y=140)

        tk.Label(self.root, text='Nivel: ').place(x=20, y=180)
        self.txt_nivel = tk.Entry(self.root, state=tk.DISABLED)
        self.txt_nivel.place(x=120, y=180)

        #BUTTONS
        
        self.btn_search = tk.Button(self.root, text='BUSCAR', command=self.search_carrers)
        self.btn_search.place(x=350, y=55)

        self.btn_new = tk.Button(self.root, text='NUEVO', command=self.new_carrers, state=tk.NORMAL)
        self.btn_new.place(x=50, y=220)

        self.btn_save = tk.Button(self.root, text='GUARDAR', command=self.save_carrers, state=tk.DISABLED)
        self.btn_save.place(x=120, y=220)

        self.btn_edit = tk.Button(self.root, text='EDITAR', command=self.edit_carrers, state=tk.DISABLED)
        self.btn_edit.place(x=205, y=220)

        self.btn_cancel = tk.Button(self.root, text='CANCELAR', command=self.principal_state, state=tk.DISABLED)
        self.btn_cancel.place(x=275, y=220)

        self.btn_delete = tk.Button(self.root, text='ELIMINAR', command=self.delete_carrers, state=tk.DISABLED)
        self.btn_delete.place(x=365, y=220) 

    def principal_state(self):
        self.txt_clave.delete(0, tk.END)
        self.txt_nombre.delete(0, tk.END)
        self.txt_nivel.delete(0, tk.END)

        self.txt_clave['state'] = tk.DISABLED
        self.txt_nombre['state'] = tk.DISABLED
        self.txt_nivel['state'] = tk.DISABLED

        self.btn_new['state'] = tk.NORMAL
        self.btn_save['state'] = tk.DISABLED
        self.btn_edit['state'] = tk.DISABLED
        self.btn_cancel['state'] = tk.DISABLED
        self.btn_delete['state'] = tk.DISABLED
    
    def search_carrers(self):
        if(len(self.txt_clave_search.get())!=0):
            query = f"SELECT * FROM carreras WHERE clave='{self.txt_clave_search.get()}'"
            with Connection.get_connection() as cnn:
                with cnn.cursor() as cursor:
                    cursor.execute(query)
                    data = cursor.fetchall()
                    print(data)
                    if not data:
                        messagebox.showwarning(title='ALERTA',message='¡No se ha encontrado registro con ese Codigo!')
                        self.principal_state()
                    else:
                        self.txt_clave.delete(0, tk.END)
                        self.txt_nombre.delete(0, tk.END)
                        self.txt_nivel.delete(0, tk.END)

                        self.txt_clave['state'] = tk.NORMAL
                        self.txt_nombre['state'] = tk.NORMAL
                        self.txt_nivel['state'] = tk.NORMAL

                        self.btn_edit['state'] = tk.NORMAL
                        self.btn_delete['state'] = tk.NORMAL
                        self.btn_cancel['state'] = tk.NORMAL

                        self.txt_clave.insert(0, data[0][0])
                        self.txt_nombre.insert(0, data[0][1])
                        self.txt_nivel.insert(0, data[0][2])

                        self.btn_new['state'] = tk.DISABLED
                        self.btn_save['state'] = tk.DISABLED
                        self.btn_edit['state'] = tk.NORMAL
                        self.btn_cancel['state'] = tk.NORMAL
                        self.btn_delete['state'] = tk.NORMAL

        else:
            messagebox.showerror(message='ERROR: Llena el campo Clave para buscar')
            self.principal_state()

    def new_carrers(self):
        self.txt_clave['state'] = tk.NORMAL
        self.txt_nombre['state'] = tk.NORMAL
        self.txt_nivel['state'] = tk.NORMAL

        self.btn_new['state'] = tk.DISABLED
        self.btn_save['state'] = tk.NORMAL
        self.btn_edit['state'] = tk.NORMAL
        self.btn_cancel['state'] = tk.NORMAL
        self.btn_delete['state'] = tk.NORMAL
        

    def save_carrers(self):
        if(len(self.txt_clave.get()) != 0 and len(self.txt_nombre.get()) != 0 and len(self.txt_nivel.get()) != 0):
            with Connection.get_connection() as cnn:
                with cnn.cursor() as cursor:
                    query = f"""INSERT INTO carreras(clave, nombre, nivel) VALUES ('{self.txt_clave.get()}', '{self.txt_nombre.get()}', '{self.txt_nivel.get()}')"""
                    cursor.execute(query)
            messagebox.showinfo(message='¡Administrador AGREGADO exitosamente!')
            self.principal_state()
        else:
            messagebox.showerror(message='ERORR: Todos los campos deben llenarse')
            self.principal_state()

    def edit_carrers(self):
        if(len(self.txt_clave.get()) != 0 and len(self.txt_nombre.get()) != 0 and len(self.txt_nivel.get()) != 0):
            with Connection.get_connection() as cnn:
                with cnn.cursor() as cursor:
                    query = f"""UPDATE carreras SET nombre = '{self.txt_nombre.get()}', nivel = '{self.txt_nivel.get()}' WHERE clave = '{self.txt_clave.get()}'"""
                    cursor.execute(query)
            messagebox.showinfo(message='¡Administrador AGREGADO exitosamente!')
            self.principal_state()
        else:
            messagebox.showerror(message='ERORR: Todos los campos deben llenarse')
            self.principal_state()

    def delete_carrers(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = Carrers(root, 'Prueba')
    root.mainloop()