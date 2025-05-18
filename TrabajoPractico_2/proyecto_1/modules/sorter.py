
# modules/sorting/sorter.py
from abc import ABC, abstractmethod
from typing import List

class Sorter(ABC):
    @abstractmethod
    def sort(self, data: List[int]) -> List[int]:
        """Devuelve una nueva lista ordenada."""
        pass
