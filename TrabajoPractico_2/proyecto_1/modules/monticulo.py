
#el monticulo esta compuesto por listas de python

import heapq

class monticulo():
    def __init__(self):
        self._heap = []
    def agregar_paciente(self, paciente):
        # Almacenamos tuplas (prioridad, paciente) para el ordenamiento
        heapq.heappush(self._heap, (paciente.get_riesgo(), paciente))# recibe [1, 2, 3] y debe recibir un int entre 1 y 3

    def obtener_siguiente(self):
        if not self._heap:
            return None
        return heapq.heappop(self._heap)[1]  # Extraemos el paciente

    def __len__(self):
        return len(self._heap)

