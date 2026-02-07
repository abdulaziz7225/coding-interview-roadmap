from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_of_pairs = 0
        for num in nums:
            xor_of_pairs ^= num

        diff_bit = 1
        while not (xor_of_pairs & diff_bit):
            diff_bit = diff_bit << 1

        first = 0
        second = 0
        for num in nums:
            if num & diff_bit:
                first ^= num
            else:
                second ^= num
        
        return [first, second]

# Time Complexity: O(n)
# Space Complexity: O(1)
