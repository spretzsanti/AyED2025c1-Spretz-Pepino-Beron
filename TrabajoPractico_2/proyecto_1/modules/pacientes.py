# -*- coding: utf-8 -*-

from random import randint, choices

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    def __init__(self, orden_de_llegada):
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]
        self.__posicion_en_la_fila = orden_de_llegada

    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_riesgo(self):
        return self.__riesgo
    
    def get_descripcion_riesgo(self):
        return self.__descripcion
    
    def __str__(self):
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion
        cad += ' ' + str(self.__posicion_en_la_fila)
        return cad
        
    def devolver_orden_llegada(self):
        return self.__posicion_en_la_fila


    def __lt__(self, other):# esto es una sobrecarga que permite comparar el orden de llegada de los pacientes
                            ##tener en cuenta prioridad y orden de llegada
        if  self.__riesgo != other.get_riesgo():
            return self.__riesgo < other.get_riesgo()
        else:
            return self.devolver_orden_llegada() < other.devolver_orden_llegada()
        

if __name__ == "__main__":
    p1 = Paciente(1)
    p2 = Paciente(4)

    print(p1)
    print(p2)
    if p1 < p2:
        print("p1 es menor que p2")
        
        