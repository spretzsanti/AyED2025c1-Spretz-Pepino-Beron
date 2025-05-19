import unittest
from modules.cola_de_prioridad import ColaDePrioridad


# Clase auxiliar para simular pacientes
class Paciente:
    def __init__(self, riesgo):
        self.riesgo = riesgo
    
    def get_riesgo(self):
        return self.riesgo

class TestColaDePrioridad(unittest.TestCase):
    def setUp(self):
        self.cola = ColaDePrioridad()
    
    def test_cola_vacia(self):
        self.assertEqual(len(self.cola), 0)
        self.assertIsNone(self.cola.desencolar())
    
    def test_unico_paciente(self):
        paciente = Paciente(1)
        self.cola.encolar(paciente)
        self.assertEqual(len(self.cola), 1)
        self.assertEqual(self.cola.desencolar(), paciente)
        self.assertEqual(len(self.cola), 0)
    
    def test_orden_prioridad(self):
        pacientes = [
            Paciente(2),  # Moderado
            Paciente(1),  # Crítico
            Paciente(3),  # Bajo
        ]
        
        for p in pacientes:
            self.cola.encolar(p)
        
        # Deberían salir en orden: 1, 2, 3
        self.assertEqual(self.cola.desencolar().get_riesgo(), 1)
        self.assertEqual(self.cola.desencolar().get_riesgo(), 2)
        self.assertEqual(self.cola.desencolar().get_riesgo(), 3)
    
    def test_desempate_por_llegada(self):
        p1 = Paciente(1)
        p2 = Paciente(1)  # Misma prioridad que p1
        
        self.cola.encolar(p1)
        self.cola.encolar(p2)
        
        # Debe salir primero el que llegó primero
        self.assertIs(self.cola.desencolar(), p1)
        self.assertIs(self.cola.desencolar(), p2)
    
    def test_caso_complejo(self):
        pacientes = [
            Paciente(2),  # Moderado (counter=0)
            Paciente(3),  # Bajo (counter=1)
            Paciente(1),  # Crítico (counter=2)
            Paciente(1),  # Crítico (counter=3)
            Paciente(2),  # Moderado (counter=4)
        ]
        
        for p in pacientes:
            self.cola.encolar(p)
        
        # Orden esperado: 
        # 1. Paciente con prioridad 1 (counter=2)
        # 2. Paciente con prioridad 1 (counter=3)
        # 3. Paciente con prioridad 2 (counter=0)
        # 4. Paciente con prioridad 2 (counter=4)
        # 5. Paciente con prioridad 3 (counter=1)
        
        self.assertIs(self.cola.desencolar(), pacientes[2])
        self.assertIs(self.cola.desencolar(), pacientes[3])
        self.assertIs(self.cola.desencolar(), pacientes[0])
        self.assertIs(self.cola.desencolar(), pacientes[4])
        self.assertIs(self.cola.desencolar(), pacientes[1])

if __name__ == "__main__":
    unittest.main()
    #borrador