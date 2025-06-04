import unittest
from modules.monticulo import MonticuloBinario

class TestMonticuloBinario(unittest.TestCase):
    def setUp(self):
        self.monticulo = MonticuloBinario()
        self.monticulo_grande = MonticuloBinario()

    def test_monticulo_vacio(self):
        """Comportamiento de montículo vacío"""
        self.assertEqual(len(self.monticulo), 0)
        self.assertFalse(self.monticulo)
        with self.assertRaises(IndexError):
            self.monticulo.eliminarMin()

    def test_insercion_eliminacion(self):
        """Inserciones y eliminaciones básicas"""
        self.monticulo.insertar(5)
        self.monticulo.insertar(2)
        self.monticulo.insertar(8)
        
        self.assertEqual(len(self.monticulo), 3)
        self.assertEqual(self.monticulo.eliminarMin(), 2)
        self.assertEqual(self.monticulo.eliminarMin(), 5)
        self.assertEqual(self.monticulo.eliminarMin(), 8)
        self.assertEqual(len(self.monticulo), 0)

    def test_propiedad_monticulo(self):
        """Verifica propiedad de min-heap después de inserciones"""
        valores = [9, 5, 6, 2, 3]
        for v in valores:
            self.monticulo.insertar(v)
        
        # Verificar propiedad de min-heap: cada nodo es <= a sus hijos
        n = self.monticulo.tamanoActual
        for i in range(1, n//2 + 1):
            left = 2 * i
            right = 2 * i + 1
            if left <= n:
                self.assertLessEqual(self.monticulo.listaMonticulo[i], 
                                    self.monticulo.listaMonticulo[left])
            if right <= n:
                self.assertLessEqual(self.monticulo.listaMonticulo[i], 
                                    self.monticulo.listaMonticulo[right])

    def test_construir_monticulo(self):
        """Construcción eficiente desde lista"""
        valores = [9, 5, 6, 2, 3]
        self.monticulo.construirMonticulo(valores)
        
        # Verificar estructura
        self.assertEqual(len(self.monticulo), 5)
        self.assertEqual(self.monticulo.listaMonticulo[1], 2)
        self.assertEqual(self.monticulo.eliminarMin(), 2)
        self.assertEqual(self.monticulo.eliminarMin(), 3)
        self.assertEqual(self.monticulo.eliminarMin(), 5)
        self.assertEqual(self.monticulo.eliminarMin(), 6)
        self.assertEqual(self.monticulo.eliminarMin(), 9)

    def test_comportamiento_orden(self):
        """Los elementos salen en orden ascendente"""
        valores = [7, 4, 9, 1, 3, 8, 5]
        for v in valores:
            self.monticulo.insertar(v)
        
        orden_esperado = sorted(valores)
        for esperado in orden_esperado:
            self.assertEqual(self.monticulo.eliminarMin(), esperado)

    def test_rendimiento_grande(self):
        """Prueba de rendimiento con muchos elementos"""
        # Insertar 1000 elementos en orden inverso
        for i in range(1000, 0, -1):
            self.monticulo_grande.insertar(i)
        
        # Verificar que salen ordenados
        for i in range(1, 1001):
            self.assertEqual(self.monticulo_grande.eliminarMin(), i)

    def test_construccion_grande(self):
        """Construcción eficiente con muchos elementos"""
        # Crear lista de 1000 elementos desordenados
        valores = list(range(1, 1001))
        import random
        random.shuffle(valores)
        
        self.monticulo_grande.construirMonticulo(valores)
        
        # Verificar que salen ordenados
        for i in range(1, 1001):
            self.assertEqual(self.monticulo_grande.eliminarMin(), i)

if __name__ == "__main__":
    unittest.main()