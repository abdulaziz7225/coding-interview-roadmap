from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)

        even_depth = True

        while queue:
            level_size = len(queue)

            prev = float("inf")
            if even_depth:
                prev = -prev

            for _ in range(level_size):
                node = queue.popleft()

                if even_depth and (node.val % 2 == 0 or node.val <= prev):
                    return False
                if not even_depth and (node.val % 2 == 1 or node.val >= prev):
                    return False
                
                prev = node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            even_depth = not even_depth

        return True

# Time Complexity: O(n)
# Space Complexity: O(n)
