from typing import List
from heapq import heappush, heappop


# Solution 1: Min Heap
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


# Solution 2: Binary Search
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        m = len(matrix[0])

        left = matrix[0][0]
        right = matrix[n - 1][m - 1]

        while left < right:
            middle = (left + right) // 2
            count = self.countLessOrEqual(matrix, n, m, middle)
            if count < k:
                left = middle + 1
            else:
                right = middle

        # return right
        return left

    def countLessOrEqual(self, matrix: List[List[int]], n: int, m: int, target: int) -> int:
        rowID = n - 1
        colID = 0
        count = 0

        while rowID >= 0 and colID < m:
            if matrix[rowID][colID] <= target:
                count += (rowID + 1)
                colID += 1
            else:
                rowID -= 1

        return count

# n = len(rows), m = len(cols), d = maximum element - minimum element
# Time Complexity: O((n + m) * log(d))
# Space Complexity: O(1)
