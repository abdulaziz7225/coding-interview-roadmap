from typing import List


# Solution 1: Arithmetic Sum
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = n * (n + 1) // 2
        for num in nums:
            result -= num
        return result

# Time Complexity: O(n)
# Space Complexity: O(1)


# Solution 2: XOR Operation
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        for idx, num in enumerate(nums):
            result ^= (idx + 1) ^ num
        return result

# Time Complexity: O(n)
# Space Complexity: O(1)


# Solution 3: Index Operation
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for idx, num in enumerate(nums):
            result += idx - num
        return result

# Time Complexity: O(n)
# Space Complexity: O(1)


# Solution 4: Cyclic Sort
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            j = nums[i]
            if j < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i:
                return i

        return n

# Time Complexity: O(3 * n - 1) ==> O(n)
# Space Complexity: O(1)