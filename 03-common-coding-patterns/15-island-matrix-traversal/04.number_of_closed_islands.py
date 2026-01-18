from typing import List


# Solution: Iterative Depth-First Search with in-place modification
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        closed_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    closed_islands += self.dfs(grid, i, j)

        return closed_islands

    def dfs(self, grid: List[List[int]], i: int, j: int) -> bool:
        is_closed = True
        stack = [(i, j)]
        grid[i][j] = 1

        while stack:
            row, col = stack.pop()
            if row == 0 or row == len(grid) - 1 or col == 0 or col == len(grid[0]) - 1:
                is_closed = False
            directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 0:

                    grid[r][c] = 1
                    stack.append((r, c))

        return is_closed

# n = len(rows), m = len(cols)
# Time Complexity: O(n * m)
# Space Complexity: O(1)
