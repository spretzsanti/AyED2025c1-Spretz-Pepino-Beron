import unittest
from modules.cola_de_prioridad import ColaDePrioridad

class TestColaDePrioridad(unittest.TestCase):
    def setUp(self):
        # Configuración inicial para todas las pruebas
        self.cola = ColaDePrioridad()
        self.cola_personalizada = ColaDePrioridad(clave=lambda x: x["prioridad"])
    
    def test_cola_vacia(self):
        """Verifica comportamiento de cola vacía"""
        self.assertEqual(len(self.cola), 0)
        self.assertIsNone(self.cola.desencolar())
        self.assertEqual(list(self.cola), [])
    
    def test_encolar_desencolar(self):
        """Verifica encolado y desencolado básico"""
        self.cola.encolar("A")
        self.assertEqual(len(self.cola), 1)
        self.assertEqual(self.cola.desencolar(), "A")
        self.assertEqual(len(self.cola), 0)
    
    def test_ordenamiento_prioridad(self):
        """Verifica diferentes estrategias de ordenamiento por prioridad"""
        # Caso 1: Prioridad por defecto con enteros
        self.cola.encolar(3)
        self.cola.encolar(1)
        self.cola.encolar(2)
        self.assertEqual(self.cola.desencolar(), 1)
        self.assertEqual(self.cola.desencolar(), 2)
        self.assertEqual(self.cola.desencolar(), 3)
        
        # Caso 2: Prioridad personalizada con diccionarios
        self.cola_personalizada.encolar({"valor": "A", "prioridad": 3})
        self.cola_personalizada.encolar({"valor": "B", "prioridad": 1})
        self.cola_personalizada.encolar({"valor": "C", "prioridad": 2})
        self.assertEqual(self.cola_personalizada.desencolar()["valor"], "B")
        self.assertEqual(self.cola_personalizada.desencolar()["valor"], "C")
        self.assertEqual(self.cola_personalizada.desencolar()["valor"], "A")
    
    def test_empate_prioridad(self):
        """Verifica desempate por orden de llegada"""
        self.cola.encolar("X")  # Llegada 0
        self.cola.encolar("Y")  # Llegada 1
        
        # Misma prioridad (los elementos son su propia prioridad)
        self.assertEqual(self.cola.desencolar(), "X")  # Primero en llegar
        self.assertEqual(self.cola.desencolar(), "Y")
    
    def test_iterador(self):
        """Verifica que el iterador no vacía la cola"""
        self.cola.encolar(1)
        self.cola.encolar(2)
        
        # Primera iteración
        elementos = list(self.cola)
        self.assertEqual(elementos, [1, 2])
        
        # Verifica que la cola sigue intacta
        self.assertEqual(len(self.cola), 2)
        self.assertEqual(self.cola.desencolar(), 1)
        
        # Segunda iteración después de desencolar
        elementos = list(self.cola)
        self.assertEqual(elementos, [2])

if __name__ == "__main__":
    unittest.main()