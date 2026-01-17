from collections import deque
from typing import List


# Solution 1: Iterative Depth-First Search with in-place modification
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    curr_area = self.dfs(grid, i, j)
                    max_area = max(max_area, curr_area)

        return max_area

    def dfs(self, grid: List[List[int]], i: int, j: int) -> int:
        curr_area = 1
        stack = [(i, j)]
        grid[i][j] = 0

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while stack:
            row, col = stack.pop()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
                    curr_area += 1
                    grid[r][c] = 0
                    stack.append((r, c))

        return curr_area

# n = len(rows), m = len(cols)
# Time Complexity: O(2 * n * m) ==> O(n * m)
# Space Complexity: O(n * m)


# Solution 2: Iterative Breadth-First Search with in-place modification
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    curr_area = self.bfs(grid, i, j)
                    max_area = max(max_area, curr_area)

        return max_area

    def bfs(self, grid: List[List[int]], i: int, j: int) -> int:
        curr_area = 1
        queue = deque()
        queue.append((i, j))
        grid[i][j] = 0

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
                    curr_area += 1
                    grid[r][c] = 0
                    queue.append((r, c))

        return curr_area

# n = len(rows), m = len(cols)
# Time Complexity: O(2 * n * m) ==> O(n * m)
# Space Complexity: O(n * m)
