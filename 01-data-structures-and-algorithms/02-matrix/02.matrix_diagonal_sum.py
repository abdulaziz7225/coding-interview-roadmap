from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total_sum = 0
        n = len(mat)
        for i in range(n):
            total_sum += mat[i][i] + mat[i][n - i - 1]

        if n & 1 == 1:
            total_sum -= mat[n // 2][n // 2]
        return total_sum

# Time Complexity: O(n)
# Space Complexity: O(1)
