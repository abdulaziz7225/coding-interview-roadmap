from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        middle = self.findMiddleElement(head)

        front = head
        back = self.reverseLinkedList(middle)

        while front and back:
            if front.val != back.val:
                return False

            front = front.next
            back = back.next

        return True

    def findMiddleElement(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

# Time Complexity: O(3 * (n // 2)) ==> O(n)
# Space Complexity: O(1)
