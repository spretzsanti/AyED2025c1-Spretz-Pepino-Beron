# -*- coding: utf-8 -*-

from random import randint, choices

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    def __init__(self, orden_de_llegada, riesgo=None):
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        # Asignar riesgo explícito o aleatorio
        self.__riesgo = riesgo if riesgo is not None else choices(niveles_de_riesgo, probabilidades)[0]
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
                            
        if  self.__riesgo != other.get_riesgo():
            return self.__riesgo < other.get_riesgo()
        else:
            return self.devolver_orden_llegada() < other.devolver_orden_llegada()