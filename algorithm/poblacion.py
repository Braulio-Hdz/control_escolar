from algorithm.data import Data
from algorithm.oferta import Oferta
class Poblacion:
    def __init__(self, tamanio, data:Data):
        self._tamanio = tamanio
        self._data = data
        self._ofertas = []
        for i in range(0, self._tamanio): self._ofertas.append(Oferta(data).inicializar())
    
    def get_ofertas(self): return self._ofertas


if __name__ == '__main__':

    nueva_data = Data()
    nueva_poblacion = Poblacion(10, nueva_data)

    i=0
    for oferta in nueva_poblacion.get_ofertas():
        i+=1
        oferta.calcular_fitness()
        print(f'OFERTA {i}: \n{oferta}\n\n')