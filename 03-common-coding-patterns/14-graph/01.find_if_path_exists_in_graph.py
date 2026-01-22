from collections import deque
from typing import List


# Solution 1: Iterative DFS with array data structure
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjacency_list = [[] for _ in range(n)]

        for src, dest in edges:
            adjacency_list[src].append(dest)
            adjacency_list[dest].append(src)

        visited = [False] * n
        stack = [source]
        visited[source] = True

        while stack:
            curr = stack.pop()

            if curr == destination:
                return True

            for neighbor in adjacency_list[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

        return False

# n = number of edges, v = len(edges)
# Time Complexity: O(n + v)
# Space Complexity: O(n + v)


# Solution 2: Iterative BFS with set data structure
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjacency_list = [[] for _ in range(n)]

        for src, dest in edges:
            adjacency_list[src].append(dest)
            adjacency_list[dest].append(src)

        visited = set()
        queue = deque([source])
        visited.add(source)

        while queue:
            curr = queue.popleft()

            if curr == destination:
                return True

            for neighbor in adjacency_list[curr]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return False

# n = number of edges, v = len(edges)
# Time Complexity: O(n + v)
# Space Complexity: O(n + v)
