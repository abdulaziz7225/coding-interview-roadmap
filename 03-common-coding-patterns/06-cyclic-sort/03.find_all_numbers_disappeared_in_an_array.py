from typing import List


# Solution 1: Cyclic Sort
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        result = []

        while i < n:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                result.append(i + 1)

        return result

# k = count of disappeared numbers
# Time Complexity: O(3 * n - 1)
# Space Complexity: O(k)
