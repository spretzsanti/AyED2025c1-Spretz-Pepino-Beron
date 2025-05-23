
#el monticulo esta compuesto por listas de python
from modules.pacientes import Paciente

class MonticuloBinario:
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0


    def infiltArriba(self,i):
        while i // 2 > 0:
          if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
             tmp = self.listaMonticulo[i // 2]
             self.listaMonticulo[i // 2] = self.listaMonticulo[i]
             self.listaMonticulo[i] = tmp
          i = i // 2

    def insertar(self,k):
      self.listaMonticulo.append(k)
      self.tamanoActual = self.tamanoActual + 1
      self.infiltArriba(self.tamanoActual)

    def infiltAbajo(self,i):
      while (i * 2) <= self.tamanoActual:
          hm = self.hijoMin(i)
          if self.listaMonticulo[i] > self.listaMonticulo[hm]:
              tmp = self.listaMonticulo[i]
              self.listaMonticulo[i] = self.listaMonticulo[hm]
              self.listaMonticulo[hm] = tmp
          i = hm

    def hijoMin(self,i):
      if i * 2 + 1 > self.tamanoActual:
          return i * 2
      else:
          if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def eliminarMin(self):
      valorSacado = self.listaMonticulo[1]
      self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
      self.tamanoActual = self.tamanoActual - 1
      self.listaMonticulo.pop()
      self.infiltAbajo(1)
      return valorSacado

    def construirMonticulo(self,unaLista):
      i = len(unaLista) // 2
      self.tamanoActual = len(unaLista)
      self.listaMonticulo = [0] + unaLista[:]
      while (i > 0):
          self.infiltAbajo(i)
          i = i - 1

    def __len__(self):
        return self.tamanoActual

    def __bool__(self):
        return self.tamanoActual > 0

if __name__ == "__main__":
   miMonticulo = MonticuloBinario()
   miMonticulo.construirMonticulo([9,5,6,2,3])
   
   print(miMonticulo.eliminarMin())
   print(miMonticulo.eliminarMin())
   print(miMonticulo.eliminarMin())
   print(miMonticulo.eliminarMin())
   print(miMonticulo.eliminarMin())



"""
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



#el monticulo esta compuesto por listas de python

import heapq
print("1")
class monticulo():
    def __init__(self):
        self._heap = []
    print("2")
    def agregar_paciente(self, paciente):
        # Almacenamos tuplas (prioridad, paciente) para el ordenamiento
        heapq.heappush(self._heap, (paciente.get_riesgo(), paciente))# recibe [1, 2, 3] y debe recibir un int entre 1 y 3
    print("3")
    def obtener_siguiente(self):
        if not self._heap:
            return None
        return heapq.heappop(self._heap)[1]  # Extraemos el paciente
    print("4")
    def __len__(self):
        return len(self._heap)
print("5")
if __name__ == "__main__":
    print("6")
    mon = monticulo()
    import pacientes as pac
    persona = pac.Paciente()
    persona2 = pac.Paciente()
    persona3 = pac.Paciente()
    
   
    print(mon.agregar_paciente(persona))
    """
"""
    mon.agregar_paciente(persona2)
    mon.agregar_paciente(persona3)
    print(mon.obtener_siguiente)
    print(mon)
    print("7")
    """
    