from typing import List


# Solution 1: Binary Search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            left = 0
            right = len(row) - 1

            while left <= right:
                middle = (left + right) // 2
                if row[middle] == target:
                    return True
                elif row[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
        return False

# n = lens(rows), m = len(columns)
# Time Complexity: O(n * log(m))
# Space Complexity: O(1)


# Solution 2: Efficient Traversal
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        rowID = n - 1
        colID = 0

        while rowID >= 0 and colID < m:
            if matrix[rowID][colID] == target:
                return True
            elif matrix[rowID][colID] < target:
                colID += 1
            else:
                rowID -= 1

        return False

# n = lens(rows), m = len(columns)
# Time Complexity: O(n + m)
# Space Complexity: O(1)
