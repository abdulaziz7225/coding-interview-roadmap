from typing import List


class Solution:
    def sort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0

        while i < n:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        return nums

# Time Complexity: O(2 * n - 1) ==> O(n)
# Space Complexity: O(1)
