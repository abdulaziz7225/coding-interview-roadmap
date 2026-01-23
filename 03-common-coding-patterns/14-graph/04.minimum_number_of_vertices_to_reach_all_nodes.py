from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree_nodes = set()
        result = []

        for _, dest in edges:
            in_degree_nodes.add(dest)

        for i in range(n):
            if i not in in_degree_nodes:
                result.append(i)

        return result

# N = number of nodes, E = len(edges)
# Time Complexity: O(N + E)
# Space Complexity: O(N)
