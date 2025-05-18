
#cola de prioridad esta compuesta por la clase monticulo !
#cola de prioridad > monticulo > lista

import heapq
import itertools

class ColaDePrioridad:
    def __init__(self):
        self._heap = []
        self._counter = itertools.count()   # contador para romper empates

    def encolar(self, paciente):
        prioridad = paciente.get_riesgo()   # 1=crítico, 2=moderado, 3=bajo
        llegada   = next(self._counter)
        # heap sortea primero por 'prioridad' y luego por 'llegada'
        heapq.heappush(self._heap, (prioridad, llegada, paciente))

    def desencolar(self):
        if not self._heap:
            return None
        return heapq.heappop(self._heap)[2]

    def __len__(self):
        return len(self._heap)
