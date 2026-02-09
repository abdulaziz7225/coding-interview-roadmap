from typing import List
from heapq import heappop, heappush


class Solution:
    def findKLargestNumbers(self, nums: List[int], k: int):
        min_heap = []

        for num in nums:
            heappush(min_heap, num)
            if len(min_heap) > k:
                heappop(min_heap)

        return min_heap

# Time Complexity: O(n * log(k))
# Space Complexity: O(k)
