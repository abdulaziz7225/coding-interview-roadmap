class Solution:
    def decimalToBinary(self, num: int) -> str:
        stack = []
        while num > 0:
            num, r = divmod(num, 2)
            stack.append(str(r))

        n = len(stack)
        for i in range(n // 2):
            stack[i], stack[n - i - 1] = stack[n - i - 1], stack[i]

        return "".join(stack)

# Time Complexity: O(3 * log(n)) ==> O(log(n))
# Space Complexity: O(2 * log(n)) ==> O(log(n))
