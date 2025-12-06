from typing import List


class Solution:
    def sortStack(self, stack: List[int]) -> List[int]:
        temp_stack = []
        while stack:
            top_element = stack.pop()

            while temp_stack and temp_stack[-1] > top_element:
                stack.append(temp_stack.pop())

            temp_stack.append(top_element)
        return temp_stack


# Time Complexity: O(n^2)
# Space Complexity: O(n)
