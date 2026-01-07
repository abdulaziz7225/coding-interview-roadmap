from typing import Optional, List
from collections import deque


# Definition for N-ary tree node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        result = []

        queue.append(root)

        while queue:
            level_size = len(queue)
            curr_level = []

            for _ in range(level_size):
                node = queue.popleft()
                curr_level.append(node.val)

                for child in node.children:
                    queue.append(child)

            result.append(curr_level)

        return result

# Time Complexity: O(n)
# Space Complexity: O(n)
