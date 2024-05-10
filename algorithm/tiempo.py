class Tiempo:
    def __init__(self, id, tiempo):
        self._id = id
        self._tiempo = tiempo

    def get_id(self): return self._id

    def get_tiempo(self): return self._tiempo

    def __str__(self) -> str:
        return f'ID: {self.get_id()} Horario: {self.get_tiempo()}'