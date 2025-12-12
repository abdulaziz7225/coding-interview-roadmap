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
        row_len = len(matrix)
        col_len = len(matrix[0])

        row_idx = row_len - 1
        col_idx = 0

        while row_idx >= 0 and col_idx < col_len:
            if matrix[row_idx][col_idx] == target:
                return True
            elif matrix[row_idx][col_idx] < target:
                col_idx += 1
            else:
                row_idx -= 1

        return False

# n = lens(rows), m = len(columns)
# Time Complexity: O(n + m)
# Space Complexity: O(1)
