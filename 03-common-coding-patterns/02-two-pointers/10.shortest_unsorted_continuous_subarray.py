from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = n, -1
        max_val = float("-inf")
        min_val = float("inf")

        for i in range(n):
            if nums[i] >= max_val:
                max_val = nums[i]
            else:
                right = i

        for i in range(n - 1, -1, -1):
            if nums[i] <= min_val:
                min_val = nums[i]
            else:
                left = i

        return max(0, right - left + 1)

# Time Complexity: O(2 * n) ==> O(n)
# Space Complexity: O(1)
