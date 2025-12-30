from typing import List


# Solution 1: Cyclic Sort
class Solution:
    def findCorrupt(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0

        while i < n:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return [nums[i], i + 1]

        return [-1, -1]

# Time Complexity: O(3 * n - 1)
# Space Complexity: O(1)
