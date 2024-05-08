from enum import Enum
class Conflicto():
    class TipoConflicto(Enum):
        PROFESOR_CONFLICTO = 1
        SALON_CONFLICTO = 2
        NUM_ESTUDIANTES_CONFLICTO = 3
    
    def __init__(self, tc, cec) -> None:
        self._tipo_conflicto = tc
        self._conflicto_entre_clases = cec

    def get_tipo_conflicto(self): return self._tipo_conflicto
    def get_c_entre_clases(self): return self._conflicto_entre_clases

    def __str__(self):
        return str(self._tipo_conflicto)+' '+str(' and '.join(map(str, self._conflicto_entre_clases)))