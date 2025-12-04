from heapq import heapify, heappop, heappush


class Solution:
    def connectSticks(self, sticks):
        cost = 0
        heapify(sticks)

        for _ in range(len(sticks) - 1):
            curr = heappop(sticks) + heappop(sticks)
            cost += curr
            heappush(sticks, curr)

        return cost

# Time Complexity: O(n + 3 * (n - 1) * log(n)) ==> O(n * log(n))
# Space Complexity: O(1)
