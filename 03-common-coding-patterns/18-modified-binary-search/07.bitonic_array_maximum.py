from typing import List


class Solution:
    def findBitonicMax(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2
            if nums[middle] < nums[middle + 1]:
                left = middle + 1
            else:
                right = middle

        return nums[left]

# Time Complexity: O(log(n))
# Space Complexity: O(1)
