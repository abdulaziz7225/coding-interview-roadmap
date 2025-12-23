from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

# Time Complexity: O(n)
# Space Complexity: O(1)


# Find the length of a cycle in Linked List
class Solution:
    def lengthOfLoop(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return self.countCycle(slow)

        return 0

    def countCycle(self, node: Optional[ListNode]) -> int:
        count = 1

        temp = node.next
        while temp is not node:
            count += 1
            temp = temp.next

        return count

# Time Complexity: O(n)
# Space Complexity: O(1)
