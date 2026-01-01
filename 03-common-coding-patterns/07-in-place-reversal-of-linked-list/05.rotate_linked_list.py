from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        length = 1
        dummy = head
        while dummy.next:
            dummy = dummy.next
            length += 1

        k %= length
        if length < 2 or k == 0:
            return head

        curr = head
        for _ in range(length - k - 1):
            curr = curr.next

        new_head = curr.next
        curr.next = None
        dummy.next = head

        return new_head

# Time Complexity: O(n)
# Space Complexity: O(1)
