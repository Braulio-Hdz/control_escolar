class Clase:
    def __init__(self, id, dep, curso):
        self._id = id
        self._departamento = dep
        self._curso = curso
        self._profesor = None
        self._tiempo = None
        self._salon = None


    def get_id(self): return self._id
    
    def get_departamento(self): return self._departamento

    def get_curso(self): return self._curso

    def get_profesor(self): return self._profesor

    def get_tiempo(self): return self._tiempo

    def get_salon(self):return self._salon

    def set_profesor(self, p): self._profesor = p

    def set_tiempo(self, t): self._tiempo = t

    def set_salon(self, s): self._salon = s

    def __str__(self):
        return f'{self._id}, {self._curso.get_numero()}, {self._curso.get_materia()}, {self._salon.get_numero()}, {self._profesor.get_nombre()}, {self._tiempo.get_tiempo()}'