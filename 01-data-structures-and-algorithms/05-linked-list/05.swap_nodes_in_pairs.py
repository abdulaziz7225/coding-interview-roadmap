from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr and curr.next:
            temp = curr.next
            curr.next = temp.next
            prev.next = temp
            temp.next = curr

            prev = curr
            curr = curr.next

        return dummy.next

# Time Complexity: O(n)
# Space Complexity: O(1)
