from typing import List

# Solution 1: Brute Force
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        modulo = 10**9 + 7
        result = 0

        for i in range(n):
            curr = arr[i]
            for j in range(i, n):
                curr = min(curr, arr[j])
                result = (result + curr) % modulo
            
        return result

# Time Complexity: O(n^2)
# Space Complexity: O(1)


# Solution 2: Monotonic Stack
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        result = [0] * len(arr)
        modulo = 10**9 + 7

        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            j = stack[-1] if stack else -1
            result[i] = result[j] + (i - j) * arr[i]

            stack.append(i)

        return sum(result) % modulo

# Time Complexity: O(3 * n) ==> O(n)
# Space Complexity: O(n)
