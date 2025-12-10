from typing import List
from heapq import heappush, heappop


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])
        free_rooms = [intervals[0][1]]

        for i in range(1, len(intervals)):
            if free_rooms[0] <= intervals[i][0]:
                heappop(free_rooms)

            heappush(free_rooms, intervals[i][1])

        return len(free_rooms)

# Time Complexity: O(2 * n * log(n)) ==> O(n * log(n))
# In Python, the sort() method sorts a list using the Timsort algorithm which is a combination
# of Merge Sort and Insertion Sort and has O(n) additional space.
# Space Complexity: O(2 * n) ==> O(n)
