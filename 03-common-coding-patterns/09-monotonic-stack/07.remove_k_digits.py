class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        if k > 0:
            stack = stack[:-k]

        result = "".join(stack).lstrip("0")

        if not result:
            return "0"
        return result

# n = count of digits in num
# Time Complexity: O(3 * n) ==> O(n)
# Space Complexity: O(n)
