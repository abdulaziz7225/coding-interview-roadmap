from typing import List


# Solution 1: With additional data structure
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        cum_sum = 0
        for i in range(n):
            cum_sum += nums[i]
            result[i] = cum_sum
        return result

# Time complexity: O(2 * n) ==> O(n)
# Space complexity: O(n)


# Solution 2: In-place modification
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums

# Time complexity: O(n)
# Space complexity: O(n)
