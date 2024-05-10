import tkinter as tk
from tkinter import messagebox
from connection_db import Connection

class Classroom:
    def __init__(self, root, name):
        self.root = root
        self.root.title("Salones")

        self.root.geometry("500x300")
        self.root.resizable(height=False, width=False)

        self.name = name
        tk.Label(self.root, text=f'¡USUARIO ACTUAL: {self.name}!', font='Arial 10').place(x=30, y=30)

        tk.Label(self.root, text='Ingresa la abreviatura del salon: ').place(x=60, y=60)
        self.txt_salon_search = tk.Entry(self.root)
        self.txt_salon_search.place(x=230, y=60)

        tk.Label(self.root, text='Abreviatura: ').place(x=20, y=100)
        self.txt_abreviatura= tk.Entry(self.root, state=tk.DISABLED)
        self.txt_abreviatura.place(x=120, y=100)
        
        tk.Label(self.root, text='Aula: ').place(x=20, y=140)
        self.txt_salon= tk.Entry(self.root, state=tk.DISABLED)
        self.txt_salon.place(x=120, y=140)

        tk.Label(self.root, text='Edificio: ').place(x=20, y=180)
        self.txt_edificio = tk.Entry(self.root, state=tk.DISABLED)
        self.txt_edificio.place(x=120, y=180)

        tk.Label(self.root, text='Capacidad: ').place(x=280, y=100)
        self.txt_capacity = tk.Entry(self.root, state=tk.DISABLED)
        self.txt_capacity.place(x=350, y=100)


        #BUTTONS
        
        self.btn_search = tk.Button(self.root, text='BUSCAR', command=self.search_classroom)
        self.btn_search.place(x=350, y=55)

        self.btn_new = tk.Button(self.root, text='NUEVO', command=self.new_classroom, state=tk.NORMAL)
        self.btn_new.place(x=50, y=220)

        self.btn_save = tk.Button(self.root, text='GUARDAR', command=self.save_classroom, state=tk.DISABLED)
        self.btn_save.place(x=120, y=220)

        self.btn_edit = tk.Button(self.root, text='EDITAR', command=self.edit_classroom, state=tk.DISABLED)
        self.btn_edit.place(x=205, y=220)

        self.btn_cancel = tk.Button(self.root, text='CANCELAR', command=self.principal_state, state=tk.DISABLED)
        self.btn_cancel.place(x=275, y=220)

        #self.btn_delete = tk.Button(self.root, text='ELIMINAR', command=self.delete_classroom, state=tk.DISABLED)
        #self.btn_delete.place(x=365, y=220) 
    
    def principal_state(self):
        self.txt_abreviatura['state'] = tk.NORMAL

        self.txt_abreviatura.delete(0, tk.END)
        self.txt_salon.delete(0, tk.END)
        self.txt_edificio.delete(0, tk.END)
        self.txt_capacity.delete(0, tk.END)

        self.txt_abreviatura['state'] = tk.DISABLED
        self.txt_salon['state'] = tk.DISABLED
        self.txt_edificio['state'] = tk.DISABLED
        self.txt_capacity['state'] = tk.DISABLED

        self.btn_new['state'] = tk.NORMAL
        self.btn_save['state'] = tk.DISABLED
        self.btn_edit['state'] = tk.DISABLED
        self.btn_cancel['state'] = tk.DISABLED
        #self.btn_delete['state'] = tk.DISABLED

    def new_classroom(self):
        self.txt_abreviatura['state'] = tk.NORMAL
        self.txt_salon['state'] = tk.NORMAL
        self.txt_edificio['state'] = tk.NORMAL
        self.txt_capacity['state'] = tk.NORMAL

        self.txt_abreviatura.delete(0, tk.END)
        self.txt_salon.delete(0, tk.END)
        self.txt_edificio.delete(0, tk.END)
        self.txt_capacity.delete(0, tk.END)

        self.btn_new['state'] = tk.DISABLED
        self.btn_save['state'] = tk.NORMAL
        self.btn_edit['state'] = tk.NORMAL
        self.btn_cancel['state'] = tk.NORMAL
        #self.btn_delete['state'] = tk.NORMAL

    def save_classroom(self):
        if(len(self.txt_salon.get()) != 0 and len(self.txt_abreviatura.get()) != 0 and len(self.txt_edificio.get()) != 0 and len(self.txt_capacity.get()) != 0):
            with Connection.get_connection() as cnn:
                with cnn.cursor() as cursor:
                    query_validate_id = f"""SELECT abreviatura FROM salones WHERE abreviatura = '{self.txt_abreviatura.get()}' OR (edificio = '{self.txt_edificio.get()}' AND aula = '{self.txt_salon.get()}')"""
                    cursor.execute(query_validate_id)
                    abr = cursor.fetchall()
                    if not abr:    
                        query = f"""INSERT INTO salones(abreviatura, edificio, aula, capacidad) 
                                VALUES ('{self.txt_abreviatura.get()}', '{self.txt_edificio.get()}', '{self.txt_salon.get()}',
                                {self.txt_capacity.get()})"""
                        try:
                            cursor.execute(query)
                            messagebox.showinfo(message='¡Salon AGREGADO exitosamente!')
                        except:
                            messagebox.showerror(message='Datos no válidos')
                    else:
                        messagebox.showinfo(message="ERROR: YA existe este salon")
            self.principal_state()
        else:
            messagebox.showerror(message='ERORR: Todos los campos deben llenarse')
            self.principal_state()

    def edit_classroom(self):
        if(len(self.txt_salon.get()) != 0 and len(self.txt_abreviatura.get()) != 0 and len(self.txt_edificio.get()) != 0):
            with Connection.get_connection() as cnn:
                with cnn.cursor() as cursor:
                    query_validate_id = f"""SELECT abreviatura FROM salones WHERE abreviatura != '{self.txt_abreviatura.get()}' AND edificio = '{self.txt_edificio.get()}' AND aula = '{self.txt_salon.get()}'"""
                    cursor.execute(query_validate_id)
                    abr = cursor.fetchall()
                    if not abr:
                        try:
                            query = f"""UPDATE salones  SET edificio ='{self.txt_edificio.get()}', aula ='{self.txt_salon.get()}', 
                            capacidad = {self.txt_capacity.get()} WHERE abreviatura = '{self.txt_abreviatura.get()}';"""
                            cursor.execute(query)
                            messagebox.showinfo(message='¡Salon EDITADO exitosamente!')
                        except:
                            messagebox.showerror(message='Datos no válidos')
                    else:
                        messagebox.showinfo(message="ERROR: YA existe este salon")
            self.principal_state()
        else:
            messagebox.showerror(message='ERORR: Todos los campos deben llenarse')
            self.principal_state()


    def delete_classroom(self):
        pass

    def search_classroom(self):
        if(len(self.txt_salon_search.get())!=0):
            query = f"SELECT * FROM salones WHERE abreviatura='{self.txt_salon_search.get()}'"
            with Connection.get_connection() as cnn:
                with cnn.cursor() as cursor:
                    cursor.execute(query)
                    data = cursor.fetchall()
                    print(data)
                    if not data:
                        messagebox.showwarning(title='ALERTA',message='¡No se ha encontrado registro con ese Codigo!')
                        self.principal_state()
                    else:
                        self.txt_abreviatura['state'] = tk.NORMAL

                        self.txt_abreviatura.delete(0, tk.END)
                        self.txt_salon.delete(0, tk.END)
                        self.txt_edificio.delete(0, tk.END)
                        self.txt_capacity.delete(0, tk.END)

                        self.txt_salon['state'] = tk.NORMAL
                        self.txt_edificio['state'] = tk.NORMAL
                        self.txt_capacity['state'] = tk.NORMAL

                        self.btn_edit['state'] = tk.NORMAL
                        self.btn_delete['state'] = tk.NORMAL
                        self.btn_cancel['state'] = tk.NORMAL

                        self.txt_abreviatura.insert(0, data[0][0])
                        self.txt_salon.insert(0, data[0][2])
                        self.txt_edificio.insert(0, data[0][1])
                        self.txt_capacity.insert(0, data[0][3])

                        self.txt_abreviatura['state'] = tk.DISABLED

                        self.btn_new['state'] = tk.DISABLED
                        self.btn_save['state'] = tk.DISABLED
                        self.btn_edit['state'] = tk.NORMAL
                        self.btn_cancel['state'] = tk.NORMAL
                        #self.btn_delete['state'] = tk.NORMAL

        else:
            messagebox.showerror(message='ERROR: Llena el campo Codigo a buscar')
            self.principal_state()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Classroom(root, 'Prueba')
    root.mainloop()