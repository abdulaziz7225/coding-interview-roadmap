from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append((root, 0))

        max_width = 1

        while queue:
            level_size = len(queue)

            start = queue[0][1]
            end = queue[-1][1]
            max_width = max(max_width, end - start + 1)

            for _ in range(level_size):
                node, index = queue.popleft()

                if node.left:
                    queue.append((node.left, 2 * index + 1))
                if node.right:
                    queue.append((node.right, 2 * index + 2))

        return max_width

# Time Complexity: O(n)
# Space Complexity: O(n)
