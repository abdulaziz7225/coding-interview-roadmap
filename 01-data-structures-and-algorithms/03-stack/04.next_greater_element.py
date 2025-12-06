from typing import List


# Solution 1: Start from the end and store elements of array in a stack
class Solution:
    def nextLargerElement(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = [-1] * len(arr)
        stack = []  # Stores values

        for i in range(n - 1, -1, -1):
            while stack and arr[i] >= stack[-1]:
                stack.pop()

            if stack:
                result[i] = stack[-1]
            stack.append(arr[i])
        return result

# Time Complexity: O(2 * n) ==> O(n)
# Space Complexity: O(2 * n) ==> O(n)


# Solution 2: Start from the beginning and store indices of elements in a stack
class Solution:
    def nextLargerElement(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = [-1] * len(arr)
        stack = []  # Stores indices

        for i in range(n):
            while stack and arr[i] > arr[stack[-1]]:
                index_to_update = stack.pop()
                result[index_to_update] = arr[i]

            # Push current index to wait for its own next greater element
            stack.append(i)

        return result

# Time Complexity: O(2 * n) ==> O(n)
# Space Complexity: O(2 * n) ==> O(n)
