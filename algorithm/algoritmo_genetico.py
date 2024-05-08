from algorithm.poblacion import Poblacion
from algorithm.data import Data
from algorithm.oferta import Oferta

import random as rnd

class Algoritmo:

    data = Data()

    def evolucionar(self, poblacion: Poblacion):
        return self.mutar_poblacion(self.cruzar_poblacion(poblacion))
    
    def cruzar_poblacion(self, poblacion: Poblacion):

        poblacion_cruzada = Poblacion(0, self.data)

        for i in range(self.data.MEJORES_HORARIOS):
            poblacion_cruzada.get_ofertas().append(poblacion.get_ofertas()[i])

        i = self.data.MEJORES_HORARIOS
        while i < self.data.TAMANIO_POBLACION:
            cromo1 = self.torneo_sel_pob(poblacion).get_ofertas()[0]
            cromo2 = self.torneo_sel_pob(poblacion).get_ofertas()[0]
            poblacion_cruzada.get_ofertas().append(self.cruzar_cromosoma(cromo1, cromo2))
            i += 1

        return poblacion_cruzada
    
    def mutar_poblacion(self, poblacion: Poblacion):
        for i in range(self.data.MEJORES_HORARIOS, self.data.TAMANIO_POBLACION):
            self.mutar_cromosoma(poblacion.get_ofertas()[i]) 
        
        return poblacion
    
    def cruzar_cromosoma(self, cromosoma1: Oferta, cromosoma2: Oferta):
        cromosoma_cruzado = Oferta(self.data).inicializar()

        for i in range(0, len(cromosoma_cruzado.get_clases())):
            if (rnd.random() > 0.5): cromosoma_cruzado.get_clases()[i] = cromosoma1.get_clases()[i]
            else: cromosoma_cruzado.get_clases()[i] = cromosoma2.get_clases()[i]
        
        return cromosoma_cruzado

    def mutar_cromosoma(self, cromosoma_mutado: Oferta):
        cromosoma_aux = Oferta(self.data).inicializar()
        for i in range(0, len(cromosoma_mutado.get_clases())):
            if(self.data.TASA_MUTACION > rnd.random()): cromosoma_mutado.get_clases()[i] = cromosoma_aux.get_clases()[i]
        
        return cromosoma_mutado
    
    def torneo_sel_pob(self, poblacion: Poblacion):
        poblacion_torneo = Poblacion(0, self.data)
        i = 0
        while i < self.data.TAMANIO_TORNEO:
            poblacion_torneo.get_ofertas().append(poblacion.get_ofertas()[rnd.randrange(0, self.data.TAMANIO_POBLACION)])
            i += 1

        poblacion_torneo.get_ofertas().sort(key=lambda x: x.get_fitness(), reverse=True)

        return poblacion_torneo