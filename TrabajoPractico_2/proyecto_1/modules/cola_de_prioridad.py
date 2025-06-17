
#cola de prioridad esta compuesta por la clase monticulo !
#cola de prioridad > monticulo > lista

from modules.monticulo import MonticuloBinario
import itertools

class ColaDePrioridad:
    def __init__(self):
        self.monticulo = MonticuloBinario()
        self._counter = itertools.count()   # contador para romper empates

    def encolar(self, k):# k = paciente # O(log n) -> por el monticulo.insertar()
        prioridad = k.get_riesgo()   # 1=crítico, 2=moderado, 3=bajo
        llegada   = next(self._counter)
        # heap sortea primero por 'prioridad' y luego por 'llegada'
        self.monticulo.insertar( (prioridad, llegada, k) )# <- Tupla con criterios # O(log n)

    def desencolar(self):# O(log n) -> por el monticulo.eliminarMin()
        if not self.monticulo:
            return None
        return self.monticulo.eliminarMin()[2]  # <- Extraer el paciente de la tupla

    def __len__(self):
        return len(self.monticulo)

    def __iter__(self):
        """
        Iterador que recorre todos los elementos actualmente en el montículo,
        sin extraerlos. Para no vaciar el heap, devolvemos un iterador sobre
        una copia de la parte “útil” de la lista interna de MonticuloBinario.
        """
        # MonticuloBinario interna: listaMonticulo[1..tamanoActual]
        # Hacemos un slice para no alterar el heap real.
        return iter(self.monticulo.listaMonticulo[1 : self.monticulo.tamanoActual + 1])# O(n) -> porque copia una porcion de la lista, copiar n elementos requiere O(n) operaciones
    
#estatico O(1)/ dinamico: encolar/desencolar O(log n); __iter__ O(n)  