import re
import tkinter as tk
from tkinter import messagebox, ttk
from connection_db import Connection

class Course:
    def __init__(self, root, name):
        self.root = root
        self.root.title("CURSOS")

        self.root.geometry("600x300")
        self.root.resizable(height=False, width=False)

        self.name = name
        tk.Label(self.root, text=f'¡USUARIO ACTUAL: {self.name}!', font='Arial 10').place(x=30, y=30)

        tk.Label(self.root, text='Ingresa CLAVE: ').place(x=60, y=60)
        self.txt_clave_search = tk.Entry(self.root)
        self.txt_clave_search.place(x=210, y=60)

        tk.Label(self.root, text='CLAVE: ').place(x=20, y=100)
        self.txt_clave= tk.Entry(self.root, state=tk.DISABLED)
        self.txt_clave.place(x=120, y=100)

        tk.Label(self.root, text='Asignatura: ').place(x=20, y=140)
        self.txt_asignatura= tk.Entry(self.root, state=tk.DISABLED)
        self.txt_asignatura.place(x=120, y=140)
        
        tk.Label(self.root, text='Creditos: ').place(x=20, y=180)
        self.txt_creditos= tk.Entry(self.root, state=tk.DISABLED)
        self.txt_creditos.place(x=120, y=180)

        tk.Label(self.root, text='Carreras: ').place(x=310, y=100)
        self.txt_carreras = ttk.Combobox(self.root, state=tk.DISABLED)
        self.txt_carreras.place(x=410, y=100)
        query2 = "SELECT clave FROM carreras"
        with Connection.get_connection() as cnn:
            with cnn.cursor() as cursor:
                cursor.execute(query2)
                self.txt_carreras['values'] = cursor.fetchall()

        tk.Label(self.root, text='Max Alumnos: ').place(x=310, y=140)
        self.txt_max_alumnos= tk.Entry(self.root, state=tk.DISABLED)
        self.txt_max_alumnos.place(x=410, y=140)

        tk.Label(self.root, text='Area Estudio: ').place(x=310, y=180)
        self.txt_area = ttk.Combobox(self.root, state=tk.DISABLED)
        self.txt_area.place(x=410, y=180)
        query = "SELECT nombre FROM areas_estudio"
        with Connection.get_connection() as cnn:
            with cnn.cursor() as cursor:
                cursor.execute(query)
                results = cursor.fetchall()
                nombres = [resultado[0] for resultado in results]
                self.txt_area['values'] = nombres   

        #BUTTONS
        
        self.btn_search = tk.Button(self.root, text='BUSCAR', command=self.search_course)
        self.btn_search.place(x=350, y=55)

        self.btn_new = tk.Button(self.root, text='NUEVO', command=self.new_course, state=tk.NORMAL)
        self.btn_new.place(x=50, y=220)

        self.btn_save = tk.Button(self.root, text='GUARDAR', command=self.save_course, state=tk.DISABLED)
        self.btn_save.place(x=120, y=220)

        self.btn_edit = tk.Button(self.root, text='EDITAR', command=self.edit_course, state=tk.DISABLED)
        self.btn_edit.place(x=205, y=220)

        self.btn_cancel = tk.Button(self.root, text='CANCELAR', command=self.principal_state, state=tk.DISABLED)
        self.btn_cancel.place(x=275, y=220)

        self.btn_delete = tk.Button(self.root, text='ELIMINAR', command=self.delete_course, state=tk.DISABLED)
        self.btn_delete.place(x=365, y=220) 

    def principal_state(self):
        self.txt_clave['state'] = tk.NORMAL
        self.txt_asignatura['state'] = tk.NORMAL
        self.txt_creditos['state'] = tk.NORMAL
        self.txt_area['state'] = tk.NORMAL
        self.txt_max_alumnos['state'] = tk.NORMAL
        self.txt_carreras['state'] = tk.NORMAL

        self.txt_clave.delete(0, tk.END)
        self.txt_asignatura.delete(0, tk.END)
        self.txt_creditos.delete(0, tk.END)
        self.txt_area.delete(0, tk.END)
        self.txt_max_alumnos.delete(0, tk.END)
        self.txt_carreras.delete(0, tk.END)
        
        self.txt_clave['state'] = tk.DISABLED
        self.txt_asignatura['state'] = tk.DISABLED
        self.txt_creditos['state'] = tk.DISABLED
        self.txt_area['state'] = tk.DISABLED
        self.txt_max_alumnos['state'] = tk.DISABLED
        self.txt_carreras['state'] = tk.DISABLED

        self.btn_new['state'] = tk.NORMAL
        self.btn_save['state'] = tk.DISABLED
        self.btn_edit['state'] = tk.DISABLED
        self.btn_cancel['state'] = tk.DISABLED
        self.btn_delete['state'] = tk.DISABLED
        

    def search_course(self):
        if(len(self.txt_clave_search.get())!= 0):
            with Connection.get_connection() as cnn:
                with cnn.cursor() as cursor:
                    query = f"SELECT * FROM cursos WHERE clave='{self.txt_clave_search.get()}'"
                    cursor.execute(query)
                    data = cursor.fetchall()

                    if data:
                        query2 = f"""SELECT nombre  FROM areas_estudio WHERE id_areas = {data[0][1]}"""
                        cursor.execute(query2)
                        area = cursor.fetchone()[0]
                    if not data:
                        messagebox.showwarning(title='ALERTA',message='¡No se ha encontrado registro con ese Codigo!')
                        self.principal_state()
                    else:
                        self.txt_clave['state'] = tk.NORMAL
                        self.txt_asignatura['state'] = tk.NORMAL
                        self.txt_creditos['state'] = tk.NORMAL
                        self.txt_area['state'] = tk.NORMAL
                        self.txt_carreras['state'] = tk.NORMAL
                        self.txt_max_alumnos['state'] = tk.NORMAL

                        self.txt_clave.delete(0, tk.END)
                        self.txt_asignatura.delete(0, tk.END)
                        self.txt_creditos.delete(0, tk.END)
                        self.txt_area.delete(0, tk.END)
                        self.txt_carreras.delete(0, tk.END)
                        self.txt_max_alumnos.delete(0, tk.END)

                        self.txt_clave.insert(0, data[0][0])
                        self.txt_area.insert(0, area)
                        self.txt_asignatura.insert(0, data[0][2])
                        self.txt_creditos.insert(0, data[0][3])
                        self.txt_carreras.insert(0, data[0][4])
                        self.txt_max_alumnos.insert(0, data[0][5])

                        self.txt_clave['state'] = tk.DISABLED

                        self.btn_new['state'] = tk.DISABLED
                        self.btn_save['state'] = tk.DISABLED
                        self.btn_edit['state'] = tk.NORMAL
                        self.btn_cancel['state'] = tk.NORMAL
                        self.btn_delete['state'] = tk.NORMAL
        else:
            messagebox.showerror(message='ERROR: Llena el campo Codigo a buscar')
            self.principal_state()
    
    def new_course(self):
        self.txt_clave.delete(0, tk.END)
        self.txt_asignatura.delete(0, tk.END)
        self.txt_creditos.delete(0, tk.END)
        self.txt_area.delete(0, tk.END)
        self.txt_max_alumnos.delete(0, tk.END)
        self.txt_carreras.delete(0, tk.END)

        self.txt_clave['state'] = tk.NORMAL
        self.txt_asignatura['state'] = tk.NORMAL
        self.txt_creditos['state'] = tk.NORMAL
        self.txt_area['state'] = tk.NORMAL
        self.txt_max_alumnos['state'] = tk.NORMAL
        self.txt_carreras['state'] = tk.NORMAL

        self.btn_new['state'] = tk.DISABLED
        self.btn_save['state'] = tk.NORMAL
        self.btn_edit['state'] = tk.DISABLED
        self.btn_cancel['state'] = tk.NORMAL
        self.btn_delete['state'] = tk.DISABLED

    def save_course(self):
        if(len(self.txt_clave.get()) != 0 and len(self.txt_asignatura.get()) != 0 and len(self.txt_creditos.get()) != 0 and len(self.txt_area.get()) != 0 and len(self.txt_carreras.get()) != 0):
            if self.validar_clave(self.txt_clave.get()):
                with Connection.get_connection() as cnn:
                    with cnn.cursor() as cursor:
                        query = f"""SELECT COUNT(*) FROM cursos WHERE nombre = '{self.txt_asignatura.get()}' AND clave != '{self.txt_clave.get()}'"""
                        cursor.execute(query)
                        repetido = cursor.fetchone()[0]
                        print(repetido)

                        if repetido:
                            messagebox.showinfo(message='Error: El nombre ya existe')
                        else:
                            query2 = f"""SELECT id_areas FROM areas_estudio WHERE nombre = '{self.txt_area.get()}'"""
                            cursor.execute(query2)
                            area = cursor.fetchone()[0]
                            try:
                                query3 = f"""INSERT INTO cursos(clave, area, nombre, creditos, carrera, max_n_alumnos) VALUES ('{self.txt_clave.get()}', {area}, '{self.txt_asignatura.get()}', {self.txt_creditos.get()}, '{self.txt_carreras.get()}', {self.txt_max_alumnos.get()})"""  
                                cursor.execute(query3)
                            
                                messagebox.showinfo(message='¡Administrador AGREGADO exitosamente!')
                                self.principal_state()
                            except:
                                messagebox.showerror(message='ERROR: Clave ya existente o datos invalidos')
            else:
                messagebox.showerror(message='ERORR: Clave invalida')         
        else:
            messagebox.showerror(message='ERORR: Todos los campos deben llenarse')
            self.principal_state()

    def edit_course(self):
        if(len(self.txt_asignatura.get()) != 0 and len(self.txt_creditos.get()) != 0 and len(self.txt_area.get()) != 0 and len(self.txt_carreras.get()) != 0):
            with Connection.get_connection() as cnn:
                with cnn.cursor() as cursor:
                    query = f"""SELECT COUNT(*) FROM cursos WHERE nombre = '{self.txt_asignatura.get()}' AND clave != '{self.txt_clave.get()}'"""
                    cursor.execute(query)
                    repetido = cursor.fetchone()[0]
                    print(repetido)

                    if repetido:
                        messagebox.showinfo(message='Error: El nombre ya existe')
                    else:
                        query2 = f"""SELECT id_areas FROM areas_estudio WHERE nombre = '{self.txt_area.get()}'"""
                        cursor.execute(query2)
                        area = cursor.fetchone()[0]
                        
                        query3 = f"""UPDATE cursos SET area = {area}, nombre = '{self.txt_asignatura.get()}', creditos = {self.txt_creditos.get()}, carrera = '{self.txt_carreras.get()}', max_n_alumnos = {self.txt_max_alumnos.get()} WHERE clave = '{self.txt_clave_search.get()}'"""  
                        cursor.execute(query3)
                        
                        messagebox.showinfo(message='¡Administrador EDITADO exitosamente!')
                        self.principal_state()
        else:
            messagebox.showerror(message='ERORR: Todos los campos deben llenarse')
            self.principal_state()

    def delete_course(self):
        pass

    def validar_clave(self, cadena):
        patron = r"^[A-Z]{1,4}[0-9]{1,4}$"
        if re.match(patron, cadena):
            return True
        else:
            return False
    
if __name__ == "__main__":
    root = tk.Tk()
    app = Course(root, 'Prueba')
    root.mainloop()