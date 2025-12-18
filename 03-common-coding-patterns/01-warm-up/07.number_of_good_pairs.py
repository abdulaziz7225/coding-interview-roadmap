from typing import List


# Solution 1
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = dict()
        for num in nums:
            count[num] = count.get(num, 0) + 1

        result = 0
        for freq in count.values():
            result += freq * (freq - 1) // 2
        return result

# Time Complexity: O(n)
# Space Complexity: O(n)


# Solution 2
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = dict()
        result = 0

        for num in nums:
            if num in count:
                result += count[num]
            count[num] = count.get(num, 0) + 1

        return result

# Time Complexity: O(n)
# Space Complexity: O(n)
