from typing import List
from heapq import heappop, heappush


class Job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load


# Solution 1: Min Heap
class Solution:
    def findMaxCPULoad(self, jobs: List[Job]) -> int:
        jobs.sort(key=lambda x: x.start)

        min_heap = []
        max_load = 0
        curr_load = 0

        for job in jobs:
            while min_heap and min_heap[0][0] <= job.start:
                _, load = heappop(min_heap)
                curr_load -= load

            heappush(min_heap, (job.end, job.cpu_load))
            curr_load += job.cpu_load
            max_load = max(max_load, curr_load)

        return max_load

# n = len(jobs)
# Time Complexity: O(3 * n * log(n)) ==> O(n * log(n))
# Space Complexity: O(2 * n) ==> O(n)
