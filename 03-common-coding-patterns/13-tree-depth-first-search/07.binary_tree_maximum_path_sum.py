from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = root.val
        self.dfs(root)
        return self.result

    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_sum = max(0, self.dfs(root.left))
        right_sum = max(0, self.dfs(root.right))

        self.result = max(self.result, root.val + left_sum + right_sum)
        return root.val + max(left_sum, right_sum)

# Time Complexity: O(n)
# Space Complexity: O(n)
