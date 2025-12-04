class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        for char in s:
            if char in ("{", "(", "["):
                stack.append(char)
            else:
                if not stack:
                    return False
                top_item = stack.pop()
                if top_item != pairs[char]:
                    return False

        return not stack

# Time Complexity: O(n)
# Space Complexity: O(n)
