
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
    """"
    mon.agregar_paciente(persona2)
    mon.agregar_paciente(persona3)
    print(mon.obtener_siguiente)
    print(mon)
    print("7")
    """