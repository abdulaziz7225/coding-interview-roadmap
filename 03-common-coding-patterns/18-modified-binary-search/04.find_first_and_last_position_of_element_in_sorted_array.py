from typing import List


# Solution 1: Bisect left and bisect right
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        first = self.firstPosition(nums, target)
        last = self.lastPosition(nums, target)
        return [first, last]

    def firstPosition(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle

        return left if nums[left] == target else -1

    def lastPosition(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right + 1) // 2
            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle

        return right if nums[right] == target else -1


# Time Complexity: O(log(n))
# Space Complexity: O(1)

# Solution 2: Two bisect left calls
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        first = self.bisect_left(nums, target)
        if first == len(nums) or nums[first] != target:
            return [-1, -1]

        last = self.bisect_left(nums, target + 1) - 1
        return [first, last]

    def bisect_left(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle

        return left

# Time Complexity: O(log(n))
# Space Complexity: O(1)


# Solution 3: Search towards a specific direction
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.custom_binary_search(nums, target, True)
        last = self.custom_binary_search(nums, target, False)
        return [first, last]

    def custom_binary_search(self, nums: List[int], target: int, is_searching_first: bool) -> int:
        left = 0
        right = len(nums) - 1
        index = -1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                index = middle
                if is_searching_first:
                    right = middle - 1
                else:
                    left = middle + 1

        return index

# Time Complexity: O(log(n))
# Space Complexity: O(1)


# Solution 4: Binary Search Template III
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        first = self.custom_binary_search(nums, target, True)
        last = self.custom_binary_search(nums, target, False)
        return [first, last]

    def custom_binary_search(self, nums: List[int], target: int, is_searching_first: bool) -> int:
        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            middle = (left + right) // 2

            if (nums[middle] > target) or (is_searching_first and nums[middle] == target):
                right = middle
            else:
                left = middle

        if is_searching_first:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
        else:
            if nums[right] == target:
                return right
            if nums[left] == target:
                return left

        return -1

# Time Complexity: O(log(n))
# Space Complexity: O(1)
