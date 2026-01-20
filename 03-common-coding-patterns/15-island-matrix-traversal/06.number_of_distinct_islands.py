from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        self.unique_islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j)

        return len(self.unique_islands)

    def dfs(self, grid: List[List[int]], i: int, j: int) -> None:
        stack = [(i, j)]
        grid[i][j] = 0

        shape = [(0, 0)]
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while stack:
            row, col = stack.pop()

            for dr, dc in directions:
                r, c = row + dr, col + dc

                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
                    stack.append((r, c))
                    grid[r][c] = 0
                    shape.append((r - i, c - j))

        self.unique_islands.add(tuple(shape))

# m = row size of matrix, n = column size of matrix
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
