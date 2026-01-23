from typing import List


# Solution 1: Depth-First Search Approach
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        self.safe_nodes = dict()
        result = []

        for i in range(n):
            if self.dfs(i, graph):
                result.append(i)

        return result

    def dfs(self, curr_node: int, graph: List[List[int]]) -> bool:
        if curr_node in self.safe_nodes:
            return self.safe_nodes[curr_node]

        self.safe_nodes[curr_node] = False
        for neighbor in graph[curr_node]:
            if not self.dfs(neighbor, graph):
                return self.safe_nodes[neighbor]

        self.safe_nodes[curr_node] = True
        return self.safe_nodes[curr_node]

# V = number of vertices, E = number of edges
# Time Complexity: O(V + E)
# Space Complexity: O(V)

# TODO: Solution 2: Topological Sorting using BFS - Kahn's Algorithm
