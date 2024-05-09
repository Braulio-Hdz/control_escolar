import tkinter as tk
from tkinter import messagebox, ttk
from connection_db import Connection

class Registro:
    def __init__(self, root, name):
        self.root = root
        self.root.title("REGISTRO")

        self.root.geometry("1400x600")
        self.root.resizable(height=False, width=False)

        self.name = name
        tk.Label(self.root, text=f'¡USUARIO ACTUAL: {self.name}!', font='Arial 10').place(x=30, y=30)

        tk.Label(self.root, text=f'Ingresa los NRC de las materias que deseas agendar (Unicamente correspondientes a tu carrera)', font='Arial 10').place(x=30, y=60)

        tk.Label(self.root, text='NRC: ').place(x=310, y=140)
        self.txt_nrc = ttk.Combobox(self.root)
        self.txt_nrc.place(x=410, y=140)
        query = f"""SELECT carrera FROM alumnos WHERE email='{self.name}'"""
        with Connection.get_connection() as cnn:
            with cnn.cursor() as cursor:
                cursor.execute(query)
                carrera = cursor.fetchall()
                query2 = f"""SELECT o.nrc FROM ofertas o 
                    JOIN cursos c ON o.curso = c.clave AND
                    c.carrera = '{carrera[0][0]}' """
                cursor.execute(query2)
                self.txt_nrc['values'] = cursor.fetchall()

        self.save_clase = tk.Button(self.root, text='GUARDAR', command=self.save_clase)
        self.save_clase.place(x=300, y=95)

         # -------------------- TABLE --------------------------

        # Table
        estilo = ttk.Style()
        estilo.configure("Treeview.Heading", font=("Calibri", 14, 'bold'), padding=7)
        self.table = ttk.Treeview(self.root, columns=('', '', '', '', '', '', ''), show='headings')
        self.table.tag_configure('estilo_personalizado', font=('Arial', 12), background='light grey')
        self.table.grid(row=5, column=0, columnspan=2, padx=10, pady=30)
        self.table.place(x=10, y=250, height=400)
        self.table.heading('#1', text='NRC')
        self.table.heading('#2', text='Curso')
        self.table.heading('#3', text='Horario')
        self.table.heading('#4', text='Salon')
        self.table.heading('#5', text='Profesor')
        self.table.heading('#6', text='Fecha de Inicio')
        self.table.heading('#7', text='Fecha Fin')
        for i in range(1, 8):
            self.table.column(f'#{i}', anchor=tk.CENTER)


    def show_registers(self, where=""):
        registers = self.table.get_children()
        for register in registers:
            self.table.delete(register)

        with Connection.get_connection() as conn:
            with conn.cursor() as cursor:
                query = f"""SELECT codigo FROM alumnos WHERE email='{self.name}'"""
                cursor.execute(query)
                codigo = cursor.fetchall()
                query_select = f"""SELECT o.nrc, o.curso, o.horario, o.salon, o.maestro, 
                                o.fecha_inicio, o.fecha_fin FROM ofertas o 
                                JOIN registro r ON r.nrc_oferta = o.nrc AND
                                r.codigo_alumno = '{codigo[0][0]}'"""
                cursor.execute(query_select)
                data = cursor.fetchall()
                for a in (data):
                    self.table.insert('', 'end', values=a, tags='estilo_personalizado')

    def save_clase(self):
        if(len(self.txt_nrc.get()) != 0):
            error = 0
            with Connection.get_connection() as cnn:
                with cnn.cursor() as cursor:
                    query = f"""SELECT email, codigo FROM alumnos WHERE email = '{self.name}'"""
                    cursor.execute(query)
                    alumno = cursor.fetchall()

                    query = f"""SELECT * FROM registro WHERE codigo_alumno = '{alumno[0][1]}'"""
                    cursor.execute(query)
                    registro_alumno = cursor.fetchall()

                    for registro in registro_alumno:
                        if self.txt_nrc.get() in registro:
                            messagebox.showinfo(message='Error: Ya agendaste esa materia')
                            error = 1
                            break

                    if error != 1:
                        query = f"""SELECT horario, COUNT(*) AS cantidad
                                    FROM (
                                        SELECT r.codigo_alumno, r.nrc_oferta, o.horario
                                        FROM registro r
                                        JOIN ofertas o ON r.nrc_oferta = o.nrc
                                        WHERE r.codigo_alumno = '{alumno[0][1]}'
                                    ) AS subconsulta
                                    GROUP BY horario
                                    HAVING COUNT(*) > 1;"""
                        
                        cursor.execute(query)
                        data = cursor.fetchall()
                        print(data)

                        if not data:
                            query = f"INSERT INTO registro(codigo_alumno, nrc_oferta) VALUES('{alumno[0][1]}', '{self.txt_nrc.get()}')"
                            cursor.execute(query)
                            query = f"""SELECT horario, COUNT(*) AS cantidad
                                    FROM (
                                        SELECT r.codigo_alumno, r.nrc_oferta, o.horario
                                        FROM registro r
                                        JOIN ofertas o ON r.nrc_oferta = o.nrc
                                        WHERE r.codigo_alumno = '{alumno[0][1]}'
                                    ) AS subconsulta
                                    GROUP BY horario
                                    HAVING COUNT(*) > 1;"""
                        
                            cursor.execute(query)
                            data = cursor.fetchall()
                            print(data)

                            if not data:
                                pass
                            else:
                                messagebox.showinfo(message='Error: Incongruencias con los HORARIOS')
                                query = f"""DELETE FROM registro WHERE nrc_oferta = '{self.txt_nrc.get()}'"""
                                cursor.execute(query)
                        else:
                            messagebox.showinfo(message='Error: Incongruencias con los HORARIOS')
        else:
            messagebox.showinfo(message='Error: El campo NRC debe llenarse')

        self.show_registers()

if __name__ == '__main__':
    root = tk.Tk()
    app = Registro(root, 'ejemplo@alumno.com')
    root.mainloop()