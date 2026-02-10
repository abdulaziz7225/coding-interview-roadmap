from typing import List
from heapq import heappop, heappush, nsmallest


# Solution 1: Heap Priority Queue
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        result = []

        for x, y in points:
            distance = -(x**2 + y**2)
            heappush(min_heap, (distance, x, y))
            if len(min_heap) > k:
                heappop(min_heap)

        for _, x, y in min_heap:
            result.append([x, y])

        return result

# Time Complexity: O(n * log(k) + k * log(k)) ==> O(n * log(k))
# Space Complexity: O(2 * k) ==> O(k)


# Solution 2: Built-in Quickselect Algorithm
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return nsmallest(k, points, key=lambda x: x[0]**2 + x[1]**2)

# In Python, heapq.nsmallest uses a specific hybrid strategy depending on the size of
# K relative to N. It builds a Max-Heap of the first K elements. For the remaining N - K
# elements, it compares the current element to the heap's largest (top). If the new
# element is smaller, it performs a heapreplace
# Time Complexity: O(n * log(k) + k * log(k)) ==> O(n * log(k))
# Space Complexity: O(2 * k) ==> O(k)

# TODO: Solution 3: Custom Quickselect Algorithm
