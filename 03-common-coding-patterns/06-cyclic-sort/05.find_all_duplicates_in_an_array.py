from typing import List


# Solution 1: Cyclic Sort
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        duplicates = list()

        while i < n:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                duplicates.append(nums[i])

        return duplicates

# k = count of duplicate numbers
# Time Complexity: O(3 * n - 1)
# Space Complexity: O(k)
