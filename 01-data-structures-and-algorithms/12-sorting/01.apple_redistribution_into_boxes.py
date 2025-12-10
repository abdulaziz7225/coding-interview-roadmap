from typing import List
from heapq import _heapify_max, _heappop_max


# Solution 1: Sorting
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        capacity.sort(reverse=True)
        count = 0

        while total_apples > 0 and count < len(capacity):
            total_apples -= capacity[count]
            count += 1

        return count

# n = len(apple), m = len(capacity)
# Time complexity: O(n + m + m * log(m)) ==> O(n + m * log(m))
# In Python, the sort() method sorts a list using the Timsort algorithm which is a combination
# of Merge Sort and Insertion Sort and has O(n) additional space.
# Space complexity: O(m)


# Solution 2: Heap Priority Queue
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        _heapify_max(capacity)
        count = 0

        while total_apples > 0:
            total_apples -= _heappop_max(capacity)
            count += 1

        return count

# n = len(apple), m = len(capacity)
# Time complexity: O(n + m + m * log(m)) ==> O(n + m * log(m))
# Space complexity: O(1)
