from typing import List


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        intervals.sort(key=lambda x: x.start)
        result = [intervals[0]]

        for interval in intervals[1:]:
            if interval.start > result[-1].end:
                result.append(Interval(interval.start, interval.end))
            else:
                result[-1].end = max(result[-1].end, interval.end)

        return result


# Time Complexity: O(n * log(n)) + O(n) ==> O(n * log(n))
# In Python, the sort() method sorts a list using the Timsort algorithm which is a combination
# of Merge Sort and Insertion Sort and has O(n) additional space.
# Space Complexity: O(n)
