
#cola de prioridad esta compuesta por la clase monticulo !
#cola de prioridad > monticulo > lista

from modules.monticulo import MonticuloBinario
import itertools

class ColaDePrioridad:
    def __init__(self):
        self.monticulo = MonticuloBinario()
        self._counter = itertools.count()   # contador para romper empates

    def encolar(self, paciente):
        prioridad = paciente.get_riesgo()   # 1=crítico, 2=moderado, 3=bajo
        llegada   = next(self._counter)
        # heap sortea primero por 'prioridad' y luego por 'llegada'
        self.monticulo.insertar(paciente)
        #heapq.heappush(self.monticulo, (prioridad, llegada, paciente))

    def desencolar(self):
        if not self.monticulo:
            return None
        return self.monticulo.eliminarMin()#heapq.heappop(self.monticulo)[2]

    def __len__(self):
        return len(self.monticulo)
