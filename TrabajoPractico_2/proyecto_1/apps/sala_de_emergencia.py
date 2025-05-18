
#gestion de pacientes a traves del monticulo y la colas de prioridad

# -*- coding: utf-8 -*-
"""
Sala de emergencias
"""
"""
import time
import datetime
import modules.pacientes as pac
import random

n = 20  # cantidad de ciclos de simulación

cola_de_espera = list()

# Ciclo que gestiona la simulación
for i in range(n):
    # Fecha y hora de entrada de un paciente
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente un paciente por segundo
    # La criticidad del paciente es aleatoria
    paciente = pac.Paciente()
    cola_de_espera.append(paciente)

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5:
        # se atiende paciente que se encuentra al frente de la cola
        paciente_atendido = cola_de_espera.pop(0)
        print('*'*40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*'*40)
    else:
        # se continúa atendiendo paciente de ciclo anterior
        pass
    
    print()

    # Se muestran los pacientes restantes en la cola de espera
    print('Pacientes que faltan atenderse:', len(cola_de_espera))
    for paciente in cola_de_espera:
        print('\t', paciente)
    
    print()
    print('-*-'*15)
    
    time.sleep(1)

    #############################################################
    """
# modules/sala.py
import datetime
import random
from modules.pacientes import Paciente

class SalaEmergencias:
    def __init__(self, cola):
        self.cola = cola

    def nuevo_paciente(self):
        p = Paciente()
        self.cola.encolar(p)
        return p

    def atender_ciclo(self, prob=0.5):
        if random.random() < prob and len(self.cola)>0:
            return self.cola.desencolar()
        return None

    def pendientes(self):
        return len(self.cola)

    def listado(self):
        # opcional: inspeccionar cola._heap o cola interna
        pass
