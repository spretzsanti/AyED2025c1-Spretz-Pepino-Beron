import unittest
from unittest.mock import Mock
import random
from apps.sala_de_emergencia import SalaEmergencias  # Ajusta la importación
from modules.pacientes import Paciente  # Asegúrate de importar correctamente

class TestSalaEmergencias(unittest.TestCase):
    def setUp(self):
        # Mock de la cola para aislar las pruebas
        self.mock_cola = Mock()
        self.mock_cola.encolar = Mock()
        self.mock_cola.desencolar = Mock(return_value="paciente_atendido")
        self.mock_cola.__len__ = Mock(return_value=3)
        
        self.sala = SalaEmergencias(self.mock_cola)
    
    def test_nuevo_paciente(self):
        paciente = self.sala.nuevo_paciente()
        self.mock_cola.encolar.assert_called_once_with(paciente)
        self.assertIsInstance(paciente, Paciente)
    
    def test_atender_ciclo_con_exito(self):
        random.seed(1)
        resultado = self.sala.atender_ciclo(prob=0.5)
        self.assertEqual(resultado, "paciente_atendido")
        self.mock_cola.desencolar.assert_called_once()
    
    def test_atender_ciclo_sin_pacientes(self):
        self.mock_cola.__len__.return_value = 0  # Cola vacía
        random.seed(0)
        resultado = self.sala.atender_ciclo(prob=0.5)
        self.assertIsNone(resultado)
    
    def test_pendientes(self):
        self.assertEqual(self.sala.pendientes(), 3)
        self.mock_cola.__len__.assert_called()
    
    def test_atender_probabilidad_100_porciento(self):
        random.seed(1)  # random() = 0.83 (mayor que 1.0)
        resultado = self.sala.atender_ciclo(prob=1.0)
        self.assertEqual(resultado, "paciente_atendido")
   
    #Comprobar si se va a utilizar
    """def test_listado_pacientes(self): 
        # Si implementas listado(), deberías verificar la interacción con la cola
       with self.assertRaises(NotImplementedError):
            self.sala.listado()"""
 
if __name__ == "__main__":
    unittest.main(verbosity=2)#borrador