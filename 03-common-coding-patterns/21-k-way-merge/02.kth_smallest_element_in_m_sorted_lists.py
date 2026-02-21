from typing import List
from heapq import heappush, heappop


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        m = len(matrix[0])

        min_heap = []
        for rowID in range(n):
            heappush(min_heap, (matrix[rowID][0], rowID, 0))

        while k > 1:
            _, rowID, colID = heappop(min_heap)
            colID += 1

            if colID < m:
                heappush(min_heap, (matrix[rowID][colID], rowID, colID))

            k -= 1

        return min_heap[0][0]

# n = len(rows), m = len(cols)
# Time Complexity: O(n + k * log(n)) ==> O(k * log(n))
# Space Complexity: O(n)
