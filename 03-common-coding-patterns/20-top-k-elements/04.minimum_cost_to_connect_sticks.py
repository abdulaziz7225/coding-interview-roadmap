from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        total_cost = 0

        while len(sticks) > 1:
            first = heappop(sticks)
            second = heappop(sticks)

            combined_cost = first + second
            total_cost += combined_cost

            heappush(sticks, combined_cost)

        return total_cost


# Time Complexity: O(n + 2 * n * log(n)) ==> O(n * log(n))
# Space Complexity: O(1)
