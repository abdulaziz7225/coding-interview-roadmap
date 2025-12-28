from typing import List


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


# Solution 1: Linear Search
class Solution:
    def insert(self, intervals: List[Interval], newInterval: Interval) -> List[Interval]:
        result = []
        n = len(intervals)
        i = 0

        while i < n and intervals[i].end < newInterval.start:
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i].start <= newInterval.end:
            newInterval.start = min(newInterval.start, intervals[i].start)
            newInterval.end = max(newInterval.end, intervals[i].end)
            i += 1
        result.append(newInterval)

        while i < n:
            result.append(intervals[i])
            i += 1

        return result

# Time Complexity: O(n)
# Space Complexity: O(n)


# Solution 2: One-Loop
class Solution:
    def insert(self, intervals: List[Interval], newInterval: Interval) -> List[Interval]:
        result = []

        for interval in intervals:
            if interval.end < newInterval.start:
                result.append(interval)
            elif newInterval.end < interval.start:
                result.append(newInterval)
                newInterval = interval
            else:
                newInterval.start = min(newInterval.start, interval.start)
                newInterval.end = max(newInterval.end, interval.end)

        result.append(newInterval)
        return result

# Time Complexity: O(n)
# Space Complexity: O(n)
