from collections import deque
from typing import List


# Solution 1: Iterative DFS
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.size = len(isConnected)
        self.visited = [False] * self.size
        provinces = 0

        for i in range(self.size):
            if not self.visited[i]:
                provinces += 1
                self.dfs(i, isConnected)

        return provinces

    def dfs(self, starting_node: int, isConnected: List[List[int]]) -> None:
        stack = [starting_node]
        self.visited[starting_node] = True

        while stack:
            curr = stack.pop()

            for neighbor in range(self.size):
                if isConnected[curr][neighbor] == 1 and not self.visited[neighbor]:
                    self.visited[neighbor] = True
                    stack.append(neighbor)

# Time Complexity: O(n^2)
# Space Complexity: O(n)


# Solution 2: Iterative BFS
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.size = len(isConnected)
        self.visited = [False] * self.size
        provinces = 0

        for i in range(self.size):
            if not self.visited[i]:
                provinces += 1
                self.bfs(i, isConnected)

        return provinces

    def bfs(self, starting_node: int, isConnected: List[List[int]]) -> None:
        queue = deque([starting_node])
        self.visited[starting_node] = True

        while queue:
            curr = queue.popleft()

            for neighbor in range(self.size):
                if isConnected[curr][neighbor] == 1 and not self.visited[neighbor]:
                    self.visited[neighbor] = True
                    queue.append(neighbor)

# Time Complexity: O(n^2)
# Space Complexity: O(n)
