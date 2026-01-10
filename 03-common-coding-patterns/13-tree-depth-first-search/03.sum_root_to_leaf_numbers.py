from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)

    def dfs(self, root: Optional[TreeNode], curr_sum: int) -> int:
        if not root:
            return 0

        curr_sum = 10 * curr_sum + root.val
        if not root.left and not root.right:
            return curr_sum

        return self.dfs(root.left, curr_sum) + self.dfs(root.right, curr_sum)

# Time Complexity: O(n)
# Space Complexity: O(n)
