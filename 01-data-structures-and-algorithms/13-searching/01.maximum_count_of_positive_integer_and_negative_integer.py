from typing import List


# Solution 1
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negatives = self.binary_search(nums, 0, True)
        positives = len(nums) - self.binary_search(nums, 0, False)

        return max(negatives, positives)

    def binary_search(self, array: List[int], target: int, is_searching_left: bool) -> int:
        left = 0
        right = len(array) - 1

        while left <= right:
            middle = (left + right) // 2
            if array[middle] < target:
                left = middle + 1
            elif array[middle] > target:
                right = middle - 1
            else:
                if is_searching_left:
                    right = middle - 1
                else:
                    left = middle + 1

        return left

# Time Complexity: O(log(n))
# Space Complexity: O(1)


# Solution 2
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negatives = self.binary_search(nums, 0)
        positives = len(nums) - self.binary_search(nums, 1)

        return max(negatives, positives)

    def binary_search(self, array: List[int], target: int) -> int:
        left = 0
        right = len(array)

        while left < right:
            middle = (left + right) // 2
            if array[middle] < target:
                left = middle + 1
            else:
                right = middle

        return left

# Time Complexity: O(log(n))
# Space Complexity: O(1)
