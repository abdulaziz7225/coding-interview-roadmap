from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        is_ascending = nums[left] < nums[right]

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle

            if is_ascending:
                if nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                if nums[middle] > target:
                    left = middle + 1
                else:
                    right = middle - 1

        return -1

# Time Complexity: O(log(n))
# Space Complexity: O(1)
