from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)

        curr_depth = 1
        result = 1
        max_level_sum = float("-inf")

        while queue:
            level_size = len(queue)
            curr_level_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                curr_level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if curr_level_sum > max_level_sum:
                max_level_sum = curr_level_sum
                result = curr_depth

            curr_depth += 1

        return result

# Time Complexity: O(n)
# Space Complexity: O(n)
