from typing import List


# Solution 1: Cyclic Sort
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            j = nums[i] - 1
            if 0 <= j < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

# k = count of duplicate numbers
# Time Complexity: O(3 * n - 1)
# Space Complexity: O(1)
