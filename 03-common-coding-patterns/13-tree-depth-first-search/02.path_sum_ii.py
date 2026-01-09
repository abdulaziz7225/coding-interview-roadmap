from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        all_paths = []
        self.dfs(root, targetSum, [], all_paths)
        return all_paths

    def dfs(self, root: Optional[TreeNode], targetSum: int, path: List[int], all_paths: List[List[int]]) -> None:
        if not root:
            return None

        targetSum -= root.val
        path.append(root.val)

        if not root.left and not root.right:
            if targetSum == 0:
                all_paths.append(path.copy())
        else:
            self.dfs(root.left, targetSum, path, all_paths)
            self.dfs(root.right, targetSum, path, all_paths)

        path.pop()

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
