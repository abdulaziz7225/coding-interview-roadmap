from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1

        if target < letters[left] or target >= letters[right]:
            return letters[left]

        while left < right:
            middle = (left + right) // 2
            if letters[middle] <= target:
                left = middle + 1
            else:
                right = middle

        return letters[left]

# Time Complexity: O(log(n))
# Space Complexity: O(1)
