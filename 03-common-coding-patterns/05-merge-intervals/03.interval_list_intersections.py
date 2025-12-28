from typing import List


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def intervalIntersection(self, firstList: List[Interval], secondList: List[Interval]) -> List[Interval]:
        ptr1, ptr2 = 0, 0
        result = []

        while ptr1 < len(firstList) and ptr2 < len(secondList):
            a_start, a_end = firstList[ptr1].start, firstList[ptr1].end
            b_start, b_end = secondList[ptr2].start, secondList[ptr2].end

            if a_start <= b_end and b_start <= a_end:
                max_start = max(a_start, b_start)
                min_end = min(a_end, b_end)
                result.append(Interval(max_start, min_end))

            if a_end <= b_end:
                ptr1 += 1
            else:
                ptr2 += 1

        return result

# n = len(firstList), m = len(secondList)
# Time Complexity: O(n + m)
# Space Complexity: O(1)
