import unittest

from modules.monticulo import monticulo 

class Paciente:
    def __init__(self, riesgo):
        self.riesgo = riesgo
    
    def get_riesgo(self):
        return self.riesgo

class TestMonticulo(unittest.TestCase):
    def setUp(self):
        self.heap = monticulo()
    
    def test_monticulo_vacio(self):
        self.assertEqual(len(self.heap), 0)
        self.assertIsNone(self.heap.obtener_siguiente())
    
    def test_un_paciente(self):
        paciente = Paciente(1)
        self.heap.agregar_paciente(paciente)
        self.assertEqual(len(self.heap), 1)
        self.assertEqual(self.heap.obtener_siguiente(), paciente)
        self.assertEqual(len(self.heap), 0)
    
    def test_orden_prioridad(self):
        pacientes = [
            Paciente(3),  # Bajo
            Paciente(1),  # Crítico
            Paciente(2),  # Moderado
        ]
        
        for p in pacientes:
            self.heap.agregar_paciente(p)
        
        # Deberían salir en orden: 1, 2, 3
        self.assertEqual(self.heap.obtener_siguiente().get_riesgo(), 1)
        self.assertEqual(self.heap.obtener_siguiente().get_riesgo(), 2)
        self.assertEqual(self.heap.obtener_siguiente().get_riesgo(), 3)
    
    def test_misma_prioridad_error(self):
        p1 = Paciente(1)
        p2 = Paciente(1)
        self.heap.agregar_paciente(p1)
        with self.assertRaises(TypeError):
            # Error al agregar el segundo paciente (no soporta misma prioridad)
            self.heap.agregar_paciente(p2)

if __name__ == "__main__":
    unittest.main()