from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])

        length = 0
        end_point = float('-inf')

        for pair in pairs:
            if pair[0] > end_point:
                end_point = pair[1]
                length += 1

        return length

# Time Complexity: O(n * log(n) + n) ==> O(n * log(n))
# In Python, the sort() method sorts a list using the Timsort algorithm which is a combination
# of Merge Sort and Insertion Sort and has O(n) additional space.
# Space Complexity: O(n)
