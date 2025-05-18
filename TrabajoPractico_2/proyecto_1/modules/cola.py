
# modules/cola.py
from abc import ABC, abstractmethod

class Cola(ABC):
    @abstractmethod
    def encolar(self, paciente):
        pass

    @abstractmethod
    def desencolar(self):
        pass

    @abstractmethod
    def __len__(self):
        pass
