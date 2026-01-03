from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head

        while curr:
            while stack and curr.val > stack[-1].val:
                stack.pop()

            if stack:
                stack[-1].next = curr

            stack.append(curr)
            curr = curr.next

        if not stack:
            return None
        return stack[0]

# Time Complexity: O(n)
# Space Complexity: O(n)
