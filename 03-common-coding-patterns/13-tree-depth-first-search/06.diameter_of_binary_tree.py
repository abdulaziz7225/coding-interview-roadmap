from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.dfs(root)
        return self.result

    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_sum = self.dfs(root.left)
        right_sum = self.dfs(root.right)

        self.result = max(self.result, left_sum + right_sum)
        return 1 + max(left_sum, right_sum)

# Time Complexity: O(n)
# Space Complexity: O(n)
