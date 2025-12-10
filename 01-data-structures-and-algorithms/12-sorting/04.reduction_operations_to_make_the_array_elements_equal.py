from typing import List


# Solution 1
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count = dict()
        for num in nums:
            count[num] = count.get(num, 0) + 1

        unique_nums = sorted(count.keys())

        result = 0
        i = 0
        for num in unique_nums:
            result += i * count[num]
            i += 1
        return result

# Time Complexity: O(2 * n + n * log(n)) ==> O(n * log(n))
# In Python, the sort() method sorts a list using the Timsort algorithm which is a combination
# of Merge Sort and Insertion Sort and has O(n) additional space.
# Space Complexity: O(2 * n) ==> O(n)


# Solution 2
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        up = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                up += 1
            result += up
        return result

# Time Complexity: O(n + n * log(n)) ==> O(n * log(n))
# In Python, the sort() method sorts a list using the Timsort algorithm which is a combination
# of Merge Sort and Insertion Sort and has O(n) additional space.
# Space Complexity: O(n)
