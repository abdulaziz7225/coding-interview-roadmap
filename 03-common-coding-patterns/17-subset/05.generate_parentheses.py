from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.stack = []
        self.backtrack(0, 0, n)
        return self.result

    def backtrack(self, openP: int, closedP: int, n: int) -> None:
        if openP == closedP == n:
            self.result.append("".join(self.stack))
            return

        if openP < n:
            self.stack.append("(")
            self.backtrack(openP + 1, closedP, n)
            self.stack.pop()

        if closedP < openP:
            self.stack.append(")")
            self.backtrack(openP, closedP + 1, n)
            self.stack.pop()

# n = number of valid sequences
# Time Complexity: O(4^n / sqrt(n))
# Space Complexity: O(4^n / sqrt(n) + 2 * n) ==> O(4^n / sqrt(n))
