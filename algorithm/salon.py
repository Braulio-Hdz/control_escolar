class Salon:
    def __init__(self, numero, capacidad):
        self._num_salon = numero
        self._capacidad = capacidad
    
    #getters
    def get_numero(self): return self._num_salon
    
    def get_capacidad(self): return self._capacidad