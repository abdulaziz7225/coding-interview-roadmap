from typing import List


# Solution 1: Two Pointers
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1

        return -1

# n = len(nums1), m = len(nums2)
# Time Complexity: O(n + m)
# Space Complexity: O(1)


# Solution 2: Binary Search
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) > len(nums2):
            return self.getCommon(nums2, nums1)

        for num in nums1:
            if self.binary_search(nums2, num):
                return num

        return -1

    def binary_search(self, array: List[int], target: int) -> bool:
        left = 0
        right = len(array) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if array[middle] == target:
                return True
            elif array[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return False

# n = len(nums1), m = len(nums2)
# Time Complexity: O(n * log(n))
# Space Complexity: O(1)
