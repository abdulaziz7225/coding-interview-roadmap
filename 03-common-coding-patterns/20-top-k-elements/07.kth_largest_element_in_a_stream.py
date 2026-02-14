from typing import List
from heapq import heappush, heappop


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k
        for num in nums:
            heappush(self.min_heap, num)
            if len(self.min_heap) > k:
                heappop(self.min_heap)

    def add(self, val: int) -> int:
        heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)
        return self.min_heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# Time Complexity:
# __init__(): O(2 * n * log(k)) ==> O(n * log(k))
# add(): O(2 * log(k)) ==> O(log(k))
# Space Complexity: O(k)
