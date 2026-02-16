from typing import List


class Solution:
    def sumBetweenTwoKth(self, nums: List[int], k1: int, k2: int) -> int:
        nums.sort()
        return sum(nums[k1:k2 - 1])

# n = len(nums)
# Time Complexity: O(n + (k2 - k1))
# Space Complexity: O(n)
