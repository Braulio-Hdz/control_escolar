class Profesor:
    def __init__(self, id, nombre):
        self._nombre = nombre
        self._id = id
    
    #getters
    def get_id(self): return self._id

    def get_nombre(self): return self._nombre

    def __str__(self): return self._nombre