from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSuccessor(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            if node.val == key:
                if queue:
                    return queue[0]
                return None

        return None


# Time Complexity: O(n)
# Space Complexity: O(n)
