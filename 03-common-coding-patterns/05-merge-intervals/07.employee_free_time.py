from typing import List


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: List[List[Interval]]) -> List[Interval]:
        result = []
        intervals = []

        for employee in schedule:
            for interval in employee:
                intervals.append(interval)

        intervals.sort(key=lambda x: x.start)
        prev_end = intervals[0].end

        for interval in intervals[1:]:
            if interval.start > prev_end:
                result.append([prev_end, interval.start])
            prev_end = max(prev_end, interval.end)

        return result

# n = total number of intervals
# Time Complexity: O(n * log(n) + 2 * n) ==> O(n * log(n))
# Space Complexity: O(2 * n) ==> O(n)
