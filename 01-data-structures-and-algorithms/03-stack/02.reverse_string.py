class Solution:
    def reverseString(self, s: str) -> str:
        stack = list(s)
        result = []

        for i in range(len(s)):
            result.append(stack.pop())

        return "".join(result)

# Time Complexity: O(3 * n) ==> O(n)
# Space Complexity: O(2 * n) ==> O(n)
