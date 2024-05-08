class Curso:
    def __init__(self, numero, nombre, profesores, max_n_alumnos):
        self._numero = numero
        self._nombre = nombre
        self._max_n_alumnos = max_n_alumnos
        self._profesor = profesores

    def get_numero(self): return self._numero

    def get_materia(self): return self._nombre

    def get_profesores(self): return self._profesor

    def get_max_n_alumnos(self): return self._max_n_alumnos
    
    #toString
    def __str__(self): return f'ID: {self._numero} MATERIA: {self._nombre}'