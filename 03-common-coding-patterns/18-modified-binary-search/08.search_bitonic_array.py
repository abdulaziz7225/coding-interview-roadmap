from typing import List


class Solution:
    def searchBitonicArray(self, nums: List[int], target: int):
        peak = self.getPeakElement(nums)

        first_half = self.customBinarySearch(nums, target, 0, peak, True)
        if first_half != -1:
            return first_half
        return self.customBinarySearch(nums, target, peak + 1, len(nums) - 1, False)

    def getPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2
            if nums[middle] < nums[middle + 1]:
                left = middle + 1
            else:
                right = middle

        return left

    def customBinarySearch(self, nums: List[int], target: int, left: int, right: int, ascending: bool):
        while left < right:
            middle = (left + right) // 2
            if ascending:
                if nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle
            else:
                if nums[middle] > target:
                    left = middle + 1
                else:
                    right = middle

        return left if nums[left] == target else -1

# Time Complexity: O(3 * log(n)) ==> O(log(n))
# Space Complexity: O(1)
