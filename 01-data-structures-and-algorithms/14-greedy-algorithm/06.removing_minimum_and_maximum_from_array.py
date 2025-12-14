from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_index = max_index = -1
        max_num = float("-inf")
        min_num = float("inf")

        for index, num in enumerate(nums):
            if num > max_num:
                max_index = index
                max_num = num
            if num < min_num:
                min_index = index
                min_num = num

        if min_index > max_index:
            min_index, max_index = max_index, min_index

        delete_from_front = max_index + 1
        delete_from_back = len(nums) - min_index
        delete_from_both = (len(nums) - max_index) + (min_index + 1)

        return min(delete_from_front, delete_from_back, delete_from_both)

# Time Complexity: O(n)
# Space Complexity: O(1)
