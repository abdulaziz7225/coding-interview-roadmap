from typing import List
from heapq import heappop, heappush


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


# Solution 1: Min Heap
class Solution:
    def minMeetingRooms(self, meetings: List[Interval]) -> int:
        meetings.sort(key=lambda x: x.start)
        min_heap = []
        max_rooms = 0

        for meeting in meetings:
            while min_heap and min_heap[0] <= meeting.start:
                heappop(min_heap)

            heappush(min_heap, meeting.end)
            max_rooms = max(max_rooms, len(min_heap))

        return max_rooms

# n = len(meetings)
# Time Complexity: O(3 * n * log(n)) ==> O(n * log(n))
# Space Complexity: O(2 * n) ==> O(n)


# Solution 2: Min Heap with fixed window size
class Solution:
    def minMeetingRooms(self, meetings: List[Interval]) -> int:
        meetings.sort(key=lambda x: x.start)
        min_heap = []

        for meeting in meetings:
            if min_heap and min_heap[0] <= meeting.start:
                heappop(min_heap)

            heappush(min_heap, meeting.end)

        return len(min_heap)

# n = len(meetings)
# Time Complexity: O(2 * n * log(n)) ==> O(n * log(n))
# Space Complexity: O(2 * n) ==> O(n)


# Solution 3: Line Sweep
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        max_end = max(interval.end for interval in intervals)
        diff_array = [0] * (max_end + 1)

        for i in intervals:
            diff_array[i.start] += 1
            diff_array[i.end] -= 1

        curr = 0
        max_rooms = 0
        for diff in diff_array:
            curr += diff
            max_rooms = max(max_rooms, curr)

        return max_rooms

# n = len(meetings), m = max_end
# Time Complexity: O(2 * n + m) ==> O(n + m)
# Space Complexity: O(m)
