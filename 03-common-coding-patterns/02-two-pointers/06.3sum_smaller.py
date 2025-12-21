from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        count = 0

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1

        return count

# Time Complexity: O(n * log(n) + n^2) ==> O(n^2)
# In Python, the sort() method sorts a list using the Timsort algorithm and has O(n) additional space.
# Space Complexity: O(n)
