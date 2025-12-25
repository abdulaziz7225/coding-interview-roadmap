from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr_window = 0
        min_window = float("inf")

        for right in range(len(nums)):
            curr_window += nums[right]

            while left <= right and curr_window >= target:
                min_window = min(min_window, right - left + 1)
                curr_window -= nums[left]
                left += 1

        if min_window == float("inf"):
            return 0
        return min_window

# Time Complexity: O(2 * n) ==> O(n)
# Space Complexity: O(1)
