from typing import List
from heapq import heappush, heappop


# Solution 1: Binary Search Approach
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        self.starts = sorted([(interval[0], idx)
                             for idx, interval in enumerate(intervals)])

        result = []
        for _, end in intervals:
            right_interval = self.custom_binary_search(intervals, end)

            if right_interval < n:
                result.append(self.starts[right_interval][1])
            else:
                result.append(-1)

        return result

    def custom_binary_search(self, intervals: List[List[int]], end: int) -> int:
        left = 0
        right = len(intervals)

        while left < right:
            middle = (left + right) // 2
            if self.starts[middle][0] >= end:
                right = middle
            else:
                left = middle + 1

        return left

# Time Complexity: O(2 * n * log(n)) ==> O(n * log(n))
# Space Complexity: O(3 * n) ==> O(n)


# Solution 2: Two Heaps Approach
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        max_start = []
        max_end = []

        result = [-1] * n

        for idx, (start, end) in enumerate(intervals):
            heappush(max_start, (-start, idx))
            heappush(max_end, (-end, idx))

        for _ in range(n):
            end, idx = heappop(max_end)

            if -max_start[0][0] >= -end:
                start, index = heappop(max_start)

                while max_start and -max_start[0][0] >= -end:
                    start, index = heappop(max_start)

                result[idx] = index
                heappush(max_start, (start, index))

        return result

# Time Complexity: O(4 * n * log(n)) ==> O(n * log(n))
# Space Complexity: O(3 * n) ==> O(n)
