from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] > k:
                return []
            result.append(nums[i:i+3])
        return result

# n = len(nums)
# Time Complexity: O(n * log(n) + n) ==> O(n * log(n))
# In Python, the sort() method sorts a list using the Timsort algorithm which is a combination
# of Merge Sort and Insertion Sort and has O(m * n) additional space.
# Space Complexity: O(2 * n) ==> O(n)
