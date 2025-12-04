from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        index, max_ones = 0, 0

        for i, row in enumerate(mat):
            curr_ones = row.count(1)

            if curr_ones > max_ones:
                max_ones = curr_ones
                index = i

        return [index, max_ones]

# Time Complexity: O(n * m)
# Space Complexity: O(1)
