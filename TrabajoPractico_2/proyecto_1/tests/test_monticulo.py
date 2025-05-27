import unittest
from modules.cola_de_prioridad import ColaDePrioridad  # Asegurate de que este módulo exista y esté bien nombrado

class Paciente:
    def __init__(self, riesgo):
        self.riesgo = riesgo
    
    def get_riesgo(self):
        return self.riesgo

    def __str__(self):
        return f"Paciente(riesgo={self.riesgo})"

class TestColaDePrioridad(unittest.TestCase):
    def setUp(self):
        self.cola = ColaDePrioridad()

    def test_cola_vacia(self):
        self.assertEqual(len(self.cola), 0)
        self.assertIsNone(self.cola.desencolar())

    def test_un_paciente(self):
        paciente = Paciente(1)
        self.cola.encolar(paciente)
        self.assertEqual(len(self.cola), 1)
        self.assertEqual(self.cola.desencolar(), paciente)
        self.assertEqual(len(self.cola), 0)

    def test_orden_prioridad(self):
        p1 = Paciente(3)  # Bajo
        p2 = Paciente(1)  # Crítico
        p3 = Paciente(2)  # Moderado

        self.cola.encolar(p1)
        self.cola.encolar(p2)
        self.cola.encolar(p3)

        self.assertEqual(self.cola.desencolar(), p2)  # Crítico
        self.assertEqual(self.cola.desencolar(), p3)  # Moderado
        self.assertEqual(self.cola.desencolar(), p1)  # Bajo

    def test_mismo_riesgo_mantiene_orden_llegada(self):
        p1 = Paciente(1)
        p2 = Paciente(1)
        self.cola.encolar(p1)
        self.cola.encolar(p2)
        self.assertEqual(self.cola.desencolar(), p1)
        self.assertEqual(self.cola.desencolar(), p2)

if __name__ == "__main__":
    unittest.main()
