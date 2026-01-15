from typing import Optional


# Definition for doubly-linked list.
class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        left = head
        right = head

        while right.next:
            right = right.next

        while left is not right and left.prev is not right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.prev

        return True

# Time Complexity: O(n)
# Space Complexity: O(1)
