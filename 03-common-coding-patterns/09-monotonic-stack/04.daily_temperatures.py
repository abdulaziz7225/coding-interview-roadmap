from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                top_index = stack.pop()
                result[top_index] = i - top_index
            stack.append(i)

        return result

# Time Complexity: O(n)
# Space Complexity: O(n)
