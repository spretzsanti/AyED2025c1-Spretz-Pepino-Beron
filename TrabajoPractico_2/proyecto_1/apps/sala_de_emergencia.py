
#gestion de pacientes a traves del monticulo y la colas de prioridad

# -*- coding: utf-8 -*-
"""
Sala de emergencias
"""

import time
import datetime
import modules.pacientes as pac
import random

from modules.cola_de_prioridad import ColaDePrioridad  # tu envoltorio del montículo

n = 20  # cantidad de ciclos de simulación

cola_prioridad = ColaDePrioridad()  # instancia de tu cola de prioridad basada en MonticuloBinario


# Ciclo que gestiona la simulación
for i in range(n):
    orden_de_llegada = i
    # Fecha y hora de entrada de un paciente
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente un paciente por segundo
    # La criticidad del paciente es aleatoria
    paciente = pac.Paciente(orden_de_llegada)# pasamos el orden de llegada
    cola_prioridad.encolar(paciente)

    print("Pacientes ANTES de atender (en orden interno del heap):")
    for p in cola_prioridad:
        print("\t", p)

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5:
        if cola_prioridad.__len__() > 0:
            print("se ejecuto el desencolar")
            paciente_atendido = cola_prioridad.desencolar()
            # se atiende paciente que se encuentra al frente de la cola
            print('*'*40)
            print('Se atiende el paciente:', paciente_atendido)
            print('*'*40)
        else:
            # se continúa atendiendo paciente de ciclo anterior
            pass
    
    print()

    # Se muestran los pacientes restantes en la cola de espera
    print('Pacientes que faltan atenderse:', cola_prioridad.__len__())
    for paciente in cola_prioridad:
        print('\t', paciente)
        #print(paciente.devolver_orden_llegada())
    print()
    print('-*-'*15)
    
    time.sleep(1)