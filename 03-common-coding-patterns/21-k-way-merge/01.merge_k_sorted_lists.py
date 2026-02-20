from typing import List, Optional
from heapq import heappush, heappop


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1: Heap Priority Queue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for index, node in enumerate(lists):
            if not node:
                continue
            heappush(min_heap, (node.val, index, node))

        dummy = ListNode(0)
        curr = dummy

        while min_heap:
            _, index, node = heappop(min_heap)

            curr.next = node
            curr = curr.next

            if node.next:
                heappush(min_heap, (node.next.val, index, node.next))

        return dummy.next

# n = total count of numbers, k = number of linked lists
# Time Complexity: O(k * log(k) + (n - k) * log(k)) ==> O(n * log(k))
# Space Complexity: O(k)


# Solution 2: Merge two linked lists at a time
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_lists = []

            for index in range(0, len(lists), 2):
                list1 = lists[index]
                list2 = lists[index + 1] if index + 1 < len(lists) else None
                merged_lists.append(self.mergeTwoSortedLists(list1, list2))

            lists = merged_lists

        return lists[0]

    def mergeTwoSortedLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return dummy.next

# n = total count of numbers, k = number of linked lists
# Time Complexity: O(n * log(k))
# Space Complexity: O(k)
