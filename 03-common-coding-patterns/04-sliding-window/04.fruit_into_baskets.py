from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        count = dict()

        for right in range(len(fruits)):
            count[fruits[right]] = count.get(fruits[right], 0) + 1

            if len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1

        return right - left + 1

# Time Complexity: O(n)
# Space Complexity: O(1)
