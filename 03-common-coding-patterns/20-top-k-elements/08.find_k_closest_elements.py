from typing import List
from heapq import heappush, heappop


# Solution 1: Heap Priority Queue
class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        max_heap = []
        for num in nums:
            heappush(max_heap, (-abs(num - x), -num))
            if len(max_heap) > k:
                heappop(max_heap)

        result = []
        for _, num in max_heap:
            result.append(-num)

        result.sort()
        return result

# n = len(nums)
# Time Complexity: O((n + k) * log(k) + k) ==> O((n + k) * log(k))
# Space Complexity: O(2 * k) ==> O(k)


# Solution 2: Binary Search
class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(nums) - k

        while left < right:
            middle = (left + right) // 2
            if x - nums[middle] > nums[middle + k] - x:
                left = middle + 1
            else:
                right = middle

        return nums[left:left + k]

# n = len(nums)
# Time Complexity: O(log(n - k) + k) ==> O(log(n) + k)
# Space Complexity: O(k)
