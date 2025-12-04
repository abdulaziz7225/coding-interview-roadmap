from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        left_sum = 0
        right_sum = sum(nums)

        for i in range(n):
            left_sum += nums[i]
            answer[i] = abs(right_sum - left_sum)
            right_sum -= nums[i]

        return answer

# Time complexity: O(3 * n) ==> O(n)
# Space complexity: O(n)