from algorithm.salon import Salon
from algorithm.tiempo import Tiempo
from algorithm.profesor import Profesor
from algorithm.curso import Curso
from algorithm.departamento import Departamento
from connection_db import Connection
from collections import defaultdict

import pandas as pd

class Data:  
    def __init__(self) -> None:
        self.TAMANIO_POBLACION = 10
        self.MEJORES_HORARIOS = 1
        self.TAMANIO_TORNEO = 3
        self.TASA_MUTACION = 0.1

        self._salones = []
        self._tiempos = []
        self._profesores = []
        self._cursos = []
        self._departamentos = []

        with Connection.get_connection() as cnn:
            with cnn.cursor() as cursor:
                query = "SELECT abreviatura, capacidad FROM salones"
                cursor.execute(query)
                self.SALONES = cursor.fetchall()
                query = """SELECT id, primer_dia || '-' || segundo_dia || ' ' || 
                            hora_inicio || '-' || hora_fin as tiempo
                            FROM horarios"""
                cursor.execute(query)
                self.f_TIEMPOS = cursor.fetchall()
                query = """SELECT email, nombre || ' ' || apellido_paterno || ' ' || apellido_materno as nombre
                            FROM maestros """
                cursor.execute(query)
                self.PROFESORES = cursor.fetchall()
                query = """SELECT c.clave, c.nombre, c.max_n_alumnos, a.maestro, c.area FROM cursos as c
                        JOIN areas_maestro as a ON c.area = a.areas """
                cursor.execute(query)
                cursos = cursor.fetchall()
                query = """SELECT a.nombre, c.nombre FROM areas_estudio as a
                        JOIN cursos as c ON a.id_areas = c.area """
                cursor.execute(query)
                depts = cursor.fetchall()

        materias = defaultdict(lambda: [None, None, [], None])
        # Llenar el diccionario con los datos
        for clave, nombre, cantidad, email, dept in cursos:
            materias[clave][0] = nombre
            materias[clave][1] = cantidad
            materias[clave][2].append(email)
            materias[clave][3] = dept
        # Convertir el diccionario a una lista de tuplas
        self.CURSOS = [(clave, datos[0], datos[1], datos[2], datos[3]) for clave, datos in materias.items()]

        departamentos = defaultdict(list)
        # Llenar el diccionario con los datos
        for departamento, materia in depts:
            departamentos[departamento].append(materia)
        # Convertir el diccionario a una lista de tuplas
        self.DEPARTAMENTOS = [(departamento, materias) for departamento, materias in departamentos.items()]
      
        for i in range(0, len(self.SALONES)):
            self._salones.append(Salon(self.SALONES[i][0], self.SALONES[i][1]))
        for i in range(0, len(self.f_TIEMPOS)):
            self._tiempos.append(Tiempo(self.f_TIEMPOS[i][0], self.f_TIEMPOS[i][1]))
        for i in range(0, len(self.PROFESORES)):
            self._profesores.append(Profesor(self.PROFESORES[i][0], self.PROFESORES[i][1]))
        for i in range(0, len(self.CURSOS)):
            lista_profesores = []
            for profesor in self._profesores:
                if profesor.get_id() in self.CURSOS[i][3]:
                    lista_profesores.append(profesor)
            self._cursos.append(Curso(self.CURSOS[i][0], self.CURSOS[i][1], lista_profesores, self.CURSOS[i][2]))
        for i in range(0, len(self.DEPARTAMENTOS)):
            lista_cursos = []
            for curso in self._cursos:
                if curso.get_materia() in self.DEPARTAMENTOS[i][1]:
                    lista_cursos.append(curso)
            self._departamentos.append(Departamento(self.DEPARTAMENTOS[i][0], lista_cursos))

        self._n_clases = 0
        for i in range(0, len(self._departamentos)):
            self._n_clases += len(self._departamentos[i].get_cursos())

        #for i in self._departamentos:
        #    print(i)

    '''SALONES = [['X1', 25], ['X2', 30], ['X3', 45], ['X4', 45]]
    ['X5', 35], ['X6', 40],
    ['X7', 20], ['X8', 30], ['X9', 45],
    ['X10', 20], ['X11', 30], ['X12', 40]
                

    TIEMPOS = [['t1', 'LX 09:00 - 11:00'],
               ['t2', 'LX 11:00 - 13:00'],
               ['t3', 'LX 13:00 - 15:00'],
               ['t4', 'LX 15:00 - 17:00'],
               ['t5', 'MJ 09:00 - 11:00'],
               ['t6', 'MJ 11:00 - 13:00'],
               ['t7', 'MJ 13:00 - 15:00'],
               ['t8', 'MJ 15:00 - 17:00'],
                ]
    
    PROFESORES = [['p1', 'Samuel Jackson', ['t1','t6', 't7', 't8']],
                  ['p2', 'John Smith', ['t2', 't3', 't4', 't5']],
                  ['p3', 'Maria Rodriguez', ['t1']]
                ]
    
    
                  ,
                  ['p4', 'Emily Davis'],
                  ['p5', 'Michael Johnson'],
                  ['p6', 'Sophia Brown'],
                  ['p7', 'Robert Lee'],
                  ['p8', 'Emma White'],
                  ['p9', 'Daniel Harris'],
                  ['p10', 'Olivia Wilson'],
                  ['p11', 'William Taylor'],
                  ['p12', 'Ava Thomas']
    
    def __init__(self) -> None:
        
        self.TAMANIO_POBLACION = 10
        self.MEJORES_HORARIOS = 1
        self.TAMANIO_TORNEO = 3
        self.TASA_MUTACION = 0.1

        self._salones = []
        self._TIEMPOS = []
        self._profesores = []
        for i in range(0, len(self.SALONES)):
            self._salones.append(Salon(self.SALONES[i][0], self.SALONES[i][1]))
        for i in range(0, len(self.TIEMPOS)):
            self._TIEMPOS.append(Tiempo(self.TIEMPOS[i][0], self.TIEMPOS[i][1]))
        for i in range(0, len(self.PROFESORES)):
            self._profesores.append(Profesor(self.PROFESORES[i][0], self.PROFESORES[i][1], self.PROFESORES[i][2]))

        curso1 = Curso('c1', 'Logica matematica', [self._profesores[0]], 30)
        curso2 = Curso('c2', 'Fundamentos de programacion', [self._profesores[0]], 40)
        curso3 = Curso('c3', 'Ecuaciones diferenciales', [self._profesores[0]], 30)
        curso4 = Curso('c4', 'Sistemas dgitales', [self._profesores[0]], 30)
        curso5 = Curso('c5', 'Estructura de datos', [self._profesores[1]], 30)
        curso6 = Curso('c6', 'Programación estructurada', [self._profesores[1]], 45)
        curso7 = Curso('c7', 'Fundamentos de física', [self._profesores[1]], 30)
        curso8 = Curso('c8', 'Fundamentos de programacion', [self._profesores[1]], 30)
        curso9 = Curso('c9', 'Logica matematica', [self._profesores[0], self._profesores[1], self._profesores[2]], 45)
        curso9 = Curso('c9', 'Logica matematica', [self._profesores[0], self._profesores[11]], 45)
            curso10 = Curso('c10', 'Programacion para internet', [self._profesores[2], self._profesores[4]], 25)
            curso11 = Curso('c11', 'Logica matematica', [self._profesores[0], self._profesores[1]], 30)
            curso12 = Curso('c12', 'Logica matematica', [self._profesores[0], self._profesores[1]], 30)
            curso13 = Curso('c13', 'Logica matematica', [self._profesores[0], self._profesores[1]], 30)
            curso14 = Curso('c14', 'Logica matematica', [self._profesores[0], self._profesores[1]], 30)
            curso15 = Curso('c15', 'Logica matematica', [self._profesores[0], self._profesores[1]], 30)
            curso16 = Curso('c16', 'Logica matematica', [self._profesores[0], self._profesores[1]], 30)
            curso17 = Curso('c17', 'Logica matematica', [self._profesores[0], self._profesores[1]], 30)
    
        self._CURSOS = [curso1, curso2, curso3, curso4, curso5, curso6, curso7, curso8]

        dep1 = Departamento("Programacion", [curso2, curso8, curso5, curso6])
        dep2 = Departamento("Matematicas", [curso1, curso3, curso9])
        dep3 = Departamento("Ciencias", [curso4, curso7])

        self._DEPARTAMENTOS = [dep1, dep2, dep3]

        '''
    
    def get_salones(self): return self._salones
    def get_profesores(self): return self._profesores
    def get_cursos(self): return self._cursos
    def get_departamentos(self): return self._departamentos
    def get_tiempos(self): return self._tiempos
    def get_n_clases(self): return self._n_clases

if __name__ == '__main__':

    data = Data()

    '''print(data.SALONES)
    print(data.CURSOS)
    print(data.PROFESORES)
    print(data.f_TIEMPOS)
    print(data.DEPARTAMENTOS)'''

    print(data.get_cursos())
    print(data.get_departamentos())
    print(data.get_profesores())
    print(data.get_salones())
    print(data.get_tiempos())
    print(data.get_n_clases())