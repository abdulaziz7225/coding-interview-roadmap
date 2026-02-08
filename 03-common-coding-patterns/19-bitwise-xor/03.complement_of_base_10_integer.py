# Solution 1
class Solution:
    def bitwiseComplement(self, num: int) -> int:
        mask = 1
        while mask < num:
            mask = 2 * mask + 1
        return mask - num

# Time Complexity: O(log(n))
# Space Complexity: O(1)


# Solution 2
class Solution:
    def bitwiseComplement(self, num: int) -> int:
        mask = 1
        while mask < num:
            mask = (mask << 1) + 1
        return mask ^ num

# Time Complexity: O(log(n))
# Space Complexity: O(1)
