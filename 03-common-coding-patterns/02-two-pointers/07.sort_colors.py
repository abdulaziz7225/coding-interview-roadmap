from typing import List


# Solution 1: Two-pass Approach
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        slow = 0

        for fast in range(n):
            if nums[fast] == 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1

        for fast in range(slow, n):
            if nums[fast] == 1:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1

# Time Complexity: O(2 * n) ==> O(n)
# Space Complexity: O(1)


# Solution 2: Dutch national flag problem
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j, k = 0, 0, len(nums) - 1

        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            else:
                j += 1

# Time Complexity: O(n)
# Space Complexity: O(1)
