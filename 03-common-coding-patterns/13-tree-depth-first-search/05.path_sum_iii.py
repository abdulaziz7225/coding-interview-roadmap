from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.result = 0
        self.all_paths = {0: 1}

        self.dfs(root, targetSum, 0)
        return self.result

    def dfs(self, root: Optional[TreeNode], target: int, curr_sum: int) -> bool:
        if not root:
            return

        curr_sum += root.val
        self.result += self.all_paths.get(curr_sum - target, 0)
        self.all_paths[curr_sum] = self.all_paths.get(curr_sum, 0) + 1

        self.dfs(root.left, target, curr_sum)
        self.dfs(root.right, target, curr_sum)

        self.all_paths[curr_sum] -= 1

# Time Complexity: O(n)
# Space Complexity: O(n)
