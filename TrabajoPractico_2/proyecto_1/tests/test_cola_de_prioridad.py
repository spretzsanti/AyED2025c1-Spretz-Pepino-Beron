import unittest
from modules.cola_de_prioridad import ColaDePrioridad
from modules.pacientes import Paciente

# Clase auxiliar para simular pacientes


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
            Paciente(1,2),  # Moderado
            Paciente(1,1),  # Crítico
            Paciente(1,3),  # Bajo
        ]
        
        for p in pacientes:
            self.cola.encolar(p)
        
        # Deberían salir en orden: 1, 2, 3
        self.assertEqual(self.cola.desencolar().get_riesgo(), 1)
        self.assertEqual(self.cola.desencolar().get_riesgo(), 2)
        self.assertEqual(self.cola.desencolar().get_riesgo(), 3)
    
    def test_desempate_por_llegada(self):
        p1 = Paciente(1,1)
        p2 = Paciente(2,1)  # Misma prioridad que p1
        
        self.cola.encolar(p1)
        self.cola.encolar(p2)
        
        # Debe salir primero el que llegó primero
        self.assertIs(self.cola.desencolar(), p1)
        self.assertIs(self.cola.desencolar(), p2)
    
    def test_caso_complejo(self):
        pacientes = [
            Paciente(0, riesgo=2),  # Moderado
            Paciente(1, riesgo=3),  # Bajo
            Paciente(2, riesgo=1),  # Crítico
            Paciente(3, riesgo=1),  # Crítico
            Paciente(4, riesgo=2),  # Moderado
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