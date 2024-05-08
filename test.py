from algorithm.algoritmo_genetico import Algoritmo
from algorithm.poblacion import Poblacion
from algorithm.data import Data


if __name__ == '__main__':
    data = Data()
    n_generacion = 1
    print(f'\n GENERACION #{n_generacion}')
    poblacion = Poblacion(data.TAMANIO_POBLACION, data)
    poblacion.get_ofertas().sort(key=lambda x: x.get_fitness(), reverse=True)
    for oferta in poblacion.get_ofertas():
        print(f'**OFERTA**\n{oferta}\n\n')

    genetico = Algoritmo()

    while (poblacion.get_ofertas()[0].get_fitness() != 1.0):
        if (n_generacion == 1500):
            print('\n\n****SOLUCION NO ENCONTRADA****\n\n')
            break
        n_generacion += 1
        print('---------------------------------------------------------------------------------')
        print(f'\n GENERACION #{n_generacion}')
        poblacion = genetico.evolucionar(poblacion)
        poblacion.get_ofertas().sort(key=lambda x: x.get_fitness(), reverse=True)
        for oferta in poblacion.get_ofertas():
            print(f'**OFERTA** \n{oferta}\n\n')
    
    print('\n\n')