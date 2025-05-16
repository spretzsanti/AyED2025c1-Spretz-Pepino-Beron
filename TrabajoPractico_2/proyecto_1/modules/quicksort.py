
# modules/sorting/quick_sort.py
from .sorter import Sorter
from typing import List

class QuickSort(Sorter):
    def sort(self, data: List[int]) -> List[int]:
        def _qs(arr):
            if len(arr) < 2:
                return arr
            pivot = arr[len(arr)//2]
            lo = [x for x in arr if x < pivot]
            eq = [x for x in arr if x == pivot]
            hi = [x for x in arr if x > pivot]
            return _qs(lo) + eq + _qs(hi)
        return _qs(data.copy())
