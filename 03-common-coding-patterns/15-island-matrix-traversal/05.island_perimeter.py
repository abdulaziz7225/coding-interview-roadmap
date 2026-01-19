from typing import List


# Solution 1: Recursive Depth-First Search with in-place modification
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.perimeter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j)
                    return self.perimeter

        return self.perimeter

    def dfs(self, grid: List[List[int]], i: int, j: int) -> None:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            self.perimeter += 1
            return

        if grid[i][j] == -1:
            return

        grid[i][j] = -1

        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)

# n = len(rows), m = len(cols)
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)


# Solution 2: Optimized Approach
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += 4

                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2

                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2

        return perimeter

# n = len(rows), m = len(cols)
# Time Complexity: O(n * m)
# Space Complexity: O(1)
