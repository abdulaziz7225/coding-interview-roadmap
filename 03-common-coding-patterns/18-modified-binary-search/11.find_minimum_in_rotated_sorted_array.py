from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle] <= nums[right]:
                right = middle
            else:
                left = middle + 1

        return nums[right]

# Time Complexity: O(log(n))
# Space Complexity: O(1)
