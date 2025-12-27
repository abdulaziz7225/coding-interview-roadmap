from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

        return right - left + 1

# Time Complexity: O(n)
# Space Complexity: O(1)
