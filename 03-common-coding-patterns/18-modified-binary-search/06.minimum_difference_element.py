from typing import List


class Solution:
    def searchMinDiffElement(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        if target < nums[left]:
            return nums[left]
        if target > nums[right]:
            return nums[right]

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return nums[middle]
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        if abs(nums[right] - target) <= abs(nums[left] - target):
            return nums[right]
        return nums[left]

# Time Complexity: O(log(n))
# Space Complexity: O(1)
