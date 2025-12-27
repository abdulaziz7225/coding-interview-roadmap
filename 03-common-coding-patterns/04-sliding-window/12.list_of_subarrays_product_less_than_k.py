from typing import List


class Solution:
    def listSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        result = []
        left = 0
        product = 1

        for right in range(len(nums)):
            product *= nums[right]

            while left <= right and product >= k:
                product //= nums[left]
                left += 1

            i = right
            while i >= left:
                result.append(nums[i:right + 1])
                i -= 1
        return result

# Time Complexity: O(n^3)
# Space Complexity: O(n^3)
