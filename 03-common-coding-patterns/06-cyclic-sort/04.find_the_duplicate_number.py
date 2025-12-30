from typing import List


# Solution 1: Cyclic Sort
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return nums[i]

        return n

# Time Complexity: O(3 * n - 1) ==> O(n)
# Space Complexity: O(1)


# Solution 2: Fast and Slow Pointers
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

# Time Complexity: O(3 * n - 1) ==> O(n)
# Space Complexity: O(1)
