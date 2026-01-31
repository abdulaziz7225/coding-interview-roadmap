class Solution:
    def numTrees(self, n: int) -> int:
        uniq_trees = [1] * (n + 1)

        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                total += uniq_trees[root - 1] * uniq_trees[nodes - root]
            uniq_trees[nodes] = total

        return uniq_trees[n]

# Time Complexity: O(n^2)
# Space Complexity: O(n)
