from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque()
        result = []

        queue.append(root)

        while queue:
            level_size = len(queue)
            curr_max = float("-inf")

            for _ in range(level_size):
                node = queue.popleft()
                curr_max = max(curr_max, node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(curr_max)

        return result

# Time Complexity: O(n)
# Space Complexity: O(n)
