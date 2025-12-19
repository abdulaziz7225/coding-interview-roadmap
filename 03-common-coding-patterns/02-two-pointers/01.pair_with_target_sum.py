from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            candidate = nums[left] + nums[right]
            if candidate == target:
                return [left, right]
            elif candidate < target:
                left += 1
            else:
                right -= 1

        return [-1, -1]

# Time Complexity: O(n)
# Space Complexity: O(1)
