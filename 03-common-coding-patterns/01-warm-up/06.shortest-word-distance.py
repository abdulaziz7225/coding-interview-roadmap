from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        ptr1, ptr2 = -1, -1
        distance = len(wordsDict)

        for index, word in enumerate(wordsDict):
            if word == word1:
                ptr1 = index

            if word == word2:
                ptr2 = index

            if ptr1 != -1 and ptr2 != -1:
                distance = min(distance, abs(ptr1 - ptr2))

        return distance

# Time Complexity: O(n)
# Space Complexity: O(1)
