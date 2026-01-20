from typing import List


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        self.visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in self.visited:
                    if self.dfs(grid, i, j):
                        return True
        return False

    def dfs(self, grid: List[List[str]], i: int, j: int) -> bool:
        stack = [(i, j, -1, -1)]
        self.visited.add((i, j))

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while stack:
            row, col, parent_row, parent_col = stack.pop()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == grid[row][col]:
                    if nr == parent_row and nc == parent_col:
                        continue

                    if (nr, nc) in self.visited:
                        return True

                    stack.append((nr, nc, row, col))
                    self.visited.add((nr, nc))
        return False

# n = row size of matrix, m = column size of matrix
# Time Complexity: O(2 * n * m) ==> O(n * m)
# Space Complexity: O(n * m)
