
# modules/sorting/radix_sort.py
from .sorter import Sorter
from typing import List

class RadixSort(Sorter):
    def sort(self, data: List[int]) -> List[int]:
        arr = data.copy()
        if not arr:
            return arr
        max_val = max(arr)
        exp = 1
        while max_val // exp > 0:
            buckets = [[] for _ in range(10)]
            for num in arr:
                buckets[(num // exp) % 10].append(num)
            arr = [num for bucket in buckets for num in bucket]
            exp *= 10
        return arr
