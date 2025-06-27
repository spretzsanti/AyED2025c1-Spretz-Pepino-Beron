from modules.monticulo import MonticuloBinario
import itertools

class ColaDePrioridad:
    def __init__(self, clave=None):
        self.monticulo = MonticuloBinario()
        self._counter = itertools.count()
        self.clave = clave or (lambda x: x)  # Función para obtener prioridad

    def encolar(self, elemento):
        prioridad = self.clave(elemento)
        llegada = next(self._counter)
        self.monticulo.insertar((prioridad, llegada, elemento))#log(n)

    def desencolar(self):
        if not self.monticulo:
            return None
        return self.monticulo.eliminarMin()[2]  #log(n)

    def __len__(self):
        return len(self.monticulo)

    def __iter__(self):
        return iter(item[2] for item in self.monticulo.listaMonticulo[1:self.monticulo.tamanoActual+1])#O(n)