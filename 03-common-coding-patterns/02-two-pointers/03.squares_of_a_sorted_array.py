from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = [0] * len(nums)

        for idx in range(len(nums) - 1, -1, -1):
            if abs(nums[left]) >= abs(nums[right]):
                result[idx] = nums[left] ** 2
                left += 1
            else:
                result[idx] = nums[right] ** 2
                right -= 1

        return result

# Time Complexity: O(n)
# Space Complexity: O(n)
