from typing import List
from heapq import _heapify_max, _heapreplace_max
from math import sqrt, floor


class Solution:
    def remainingGifts(self, gifts: List[int], k: int) -> int:
        _heapify_max(gifts)

        for _ in range(k):
            _heapreplace_max(gifts, floor(sqrt(gifts[0])))

        return sum(gifts)

# n = len(gifts)
# Time Complexity: O(2 * n + k * log(n)) ==> O(n + k * log(n))
# Space Complexity: O(1)
# heapify() method operates in-place and requires O(1) space complexity
