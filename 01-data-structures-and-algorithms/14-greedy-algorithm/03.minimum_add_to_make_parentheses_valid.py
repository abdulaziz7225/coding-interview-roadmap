# Solution 1: Stack
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for char in s:
            if stack and stack[-1] == "(" and char == ")":
                stack.pop()
            else:
                stack.append(char)

        return len(stack)

# Time Complexity: O(n)
# Space Complexity: O(n)


# Solution 2: Open Bracket Counter
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0
        min_add_required = 0

        for char in s:
            if char == "(":
                open_brackets += 1
            elif open_brackets > 0:
                open_brackets -= 1
            else:
                min_add_required += 1

        return open_brackets + min_add_required

# Time Complexity: O(n)
# Space Complexity: O(1)
