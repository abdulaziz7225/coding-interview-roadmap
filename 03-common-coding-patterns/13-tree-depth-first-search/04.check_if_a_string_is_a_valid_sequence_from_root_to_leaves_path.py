from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        return self.dfs(root, arr, 0)

    def dfs(self, root: Optional[TreeNode], arr: List[int], curr_index: int) -> bool:
        if not root or root.val != arr[curr_index]:
            return False

        if curr_index == len(arr) - 1:
            return not root.left and not root.right

        return self.dfs(root.left, arr, curr_index + 1) or self.dfs(root.right, arr, curr_index + 1)

# Time Complexity: O(n)
# Space Complexity: O(n)
