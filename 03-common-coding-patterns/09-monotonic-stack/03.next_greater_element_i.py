from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = dict()
        stack = []
        result = []

        for num in nums2:
            while stack and num > stack[-1]:
                top_element = stack.pop()
                next_greater[top_element] = num

            stack.append(num)

        for num in nums1:
            result.append(next_greater.get(num, -1))

        return result

# n = len(nums1), m = len(nums2) 
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
