import re
import tkinter as tk
from tkinter import messagebox, ttk
from connection_db import Connection
from datetime import datetime

class Schedule:
    def __init__(self, root, name):
        self.root = root
        self.root.title("Horarios")

        self.root.geometry("600x300")
        self.root.resizable(height=False, width=False)

        self.name = name
        tk.Label(self.root, text=f'¡USUARIO ACTUAL: {self.name}!', font='Arial 10').place(x=30, y=30)

        tk.Label(self.root, text='Ingresa el ID: ').place(x=60, y=60)
        self.txt_id_search = tk.Entry(self.root)
        self.txt_id_search.place(x=210, y=60)

        tk.Label(self.root, text='Primer Dia: ').place(x=20, y=100)
        self.txt_primer_dia= tk.Entry(self.root, state=tk.DISABLED)
        self.txt_primer_dia.place(x=120, y=100)
        
        tk.Label(self.root, text='Segundo Dia: ').place(x=20, y=140)
        self.txt_segundo_dia= tk.Entry(self.root, state=tk.DISABLED)
        self.txt_segundo_dia.place(x=120, y=140)

        tk.Label(self.root, text='Hora Inicio: ').place(x=310, y=100)
        self.txt_fecha_inicio= tk.Entry(self.root, state=tk.DISABLED)
        self.txt_fecha_inicio.place(x=410, y=100)

        tk.Label(self.root, text='Hora Fin: ').place(x=310, y=140)
        self.txt_fecha_fin= tk.Entry(self.root, state=tk.DISABLED)
        self.txt_fecha_fin.place(x=410, y=140)

        #BUTTONS

        self.btn_search = tk.Button(self.root, text='BUSCAR', command=self.search_schedule)
        self.btn_search.place(x=350, y=55)

        self.btn_new = tk.Button(self.root, text='NUEVO', command=self.new_schedule, state=tk.NORMAL)
        self.btn_new.place(x=50, y=220)

        self.btn_save = tk.Button(self.root, text='GUARDAR', command=self.save_schedule, state=tk.DISABLED)
        self.btn_save.place(x=120, y=220)

        self.btn_edit = tk.Button(self.root, text='EDITAR', command=self.edit_schedule, state=tk.DISABLED)
        self.btn_edit.place(x=205, y=220)

        self.btn_cancel = tk.Button(self.root, text='CANCELAR', command=self.principal_state, state=tk.DISABLED)
        self.btn_cancel.place(x=275, y=220)

        self.btn_delete = tk.Button(self.root, text='ELIMINAR', command=self.delete_schedule, state=tk.DISABLED)
        self.btn_delete.place(x=365, y=220) 

    def principal_state(self):
        self.txt_primer_dia.delete(0, tk.END)
        self.txt_segundo_dia.delete(0, tk.END)
        self.txt_fecha_inicio.delete(0, tk.END)
        self.txt_fecha_fin.delete(0, tk.END)

        self.txt_primer_dia['state'] = tk.DISABLED
        self.txt_segundo_dia['state'] = tk.DISABLED
        self.txt_fecha_inicio['state'] = tk.DISABLED
        self.txt_fecha_fin['state'] = tk.DISABLED

        self.btn_new['state'] = tk.NORMAL
        self.btn_save['state'] = tk.DISABLED
        self.btn_edit['state'] = tk.DISABLED
        self.btn_cancel['state'] = tk.DISABLED
        self.btn_delete['state'] = tk.DISABLED

    def search_schedule(self):
        if(len(self.txt_id_search.get())!= 0):
            with Connection.get_connection() as cnn:
                with cnn.cursor() as cursor:
                    query = f"SELECT * FROM horarios WHERE id={self.txt_id_search.get()}"
                    cursor.execute(query)
                    data = cursor.fetchall()
                    print(data)

                    if not data:
                        messagebox.showwarning(title='ALERTA',message='¡No se ha encontrado registro con ese Codigo!')
                        self.principal_state()
                    else:
                        self.txt_primer_dia['state'] = tk.NORMAL
                        self.txt_segundo_dia['state'] = tk.NORMAL
                        self.txt_fecha_inicio['state'] = tk.NORMAL
                        self.txt_fecha_fin['state'] = tk.NORMAL

                        self.txt_primer_dia.delete(0, tk.END)
                        self.txt_segundo_dia.delete(0, tk.END)
                        self.txt_fecha_inicio.delete(0, tk.END)
                        self.txt_fecha_fin.delete(0, tk.END)

                        self.txt_primer_dia.insert(0, data[0][1])
                        self.txt_segundo_dia.insert(0, data[0][2])
                        self.txt_fecha_inicio.insert(0, data[0][3])
                        self.txt_fecha_fin.insert(0, data[0][4])

                        self.btn_new['state'] = tk.DISABLED
                        self.btn_save['state'] = tk.DISABLED
                        self.btn_edit['state'] = tk.NORMAL
                        self.btn_cancel['state'] = tk.NORMAL
                        self.btn_delete['state'] = tk.NORMAL
        else:
            messagebox.showerror(message='ERROR: Llena el campo ID a buscar')
            self.principal_state()

    def new_schedule(self):
        self.txt_primer_dia['state'] = tk.NORMAL
        self.txt_segundo_dia['state'] = tk.NORMAL
        self.txt_fecha_inicio['state'] = tk.NORMAL
        self.txt_fecha_fin['state'] = tk.NORMAL

        self.btn_new['state'] = tk.DISABLED
        self.btn_save['state'] = tk.NORMAL
        self.btn_edit['state'] = tk.DISABLED
        self.btn_cancel['state'] = tk.NORMAL
        self.btn_delete['state'] = tk.DISABLED


    def save_schedule(self):
        if(len(self.txt_primer_dia.get()) != 0 and len(self.txt_segundo_dia.get()) != 0 and len(self.txt_fecha_inicio.get()) != 0 and len(self.txt_fecha_fin.get()) != 0):
            hora1_dt = datetime.strptime(self.txt_fecha_inicio.get(), '%H:%M:%S')
            hora2_dt = datetime.strptime(self.txt_fecha_fin.get(), '%H:%M:%S')

            if hora1_dt < hora2_dt and self.validar_formato_hora(self.txt_fecha_inicio.get()) and self.validar_formato_hora(self.txt_fecha_fin.get()):
                with Connection.get_connection() as cnn:
                    with cnn.cursor() as cursor:
                        query = f"""INSERT INTO horarios (primer_dia, segundo_dia, hora_inicio, hora_fin) VALUES ('{self.txt_primer_dia.get()}', '{self.txt_segundo_dia.get()}', '{self.txt_fecha_inicio.get()}', '{self.txt_fecha_fin.get()}')"""
                        print(query)
                        cursor.execute(query)
                messagebox.showinfo(message='¡Administrador AGREGADO exitosamente!')
                self.principal_state()
            else:
                messagebox.showinfo(message='ERROR: Formato de la fecha incorrecto')
        else:
            messagebox.showerror(message='ERORR: Todos los campos deben llenarse')
            self.principal_state()

    def edit_schedule(self):
        if(len(self.txt_primer_dia.get()) != 0 and len(self.txt_segundo_dia.get()) != 0 and len(self.txt_fecha_inicio.get()) != 0 and len(self.txt_fecha_fin.get()) != 0):

            hora1_dt = datetime.strptime(self.txt_fecha_inicio.get(), '%H:%M:%S')
            hora2_dt = datetime.strptime(self.txt_fecha_fin.get(), '%H:%M:%S')

            if hora1_dt < hora2_dt and self.validar_formato_hora(self.txt_fecha_inicio.get()) and self.validar_formato_hora(self.txt_fecha_fin.get()):
                with Connection.get_connection() as cnn:
                    with cnn.cursor() as cursor:
                        query = f"""UPDATE horarios SET primer_dia = '{self.txt_primer_dia.get()}', segundo_dia = '{self.txt_segundo_dia.get()}', hora_inicio = '{self.txt_fecha_inicio.get()}', hora_fin = '{self.txt_fecha_fin.get()}' WHERE id = {self.txt_id_search.get()}"""
                        print(query)
                        cursor.execute(query)
                messagebox.showinfo(message='¡Administrador AGREGADO exitosamente!')
                self.principal_state()
            else:
                messagebox.showinfo(message='ERROR: Formato de la fecha incorrecto')
        else:
            messagebox.showerror(message='ERORR: Todos los campos deben llenarse')
            self.principal_state()

    def delete_schedule(self):
        pass

    def validar_formato_hora(self, hora):
        # Patrón de expresión regular para verificar el formato HH:MM:SS
        patron = re.compile(r'^([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$')
        return bool(patron.match(hora))
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Schedule(root, 'Prueba')
    root.mainloop()