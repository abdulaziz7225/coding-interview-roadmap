# Solution 1: Stack
class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        for char in s:
            if char in vowels:
                stack.append(char)

        result = []
        for char in s:
            if char in vowels:
                result.append(stack.pop())
            else:
                result.append(char)

        return "".join(result)

# Time Complexity: O(3 * n) ==> O(n)
# Space Complexity: O(n)


# Solution 2: Two Pointers
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        array = list(s)
        left = 0
        right = len(array) - 1

        while left < right:
            while left < right and array[left] not in vowels:
                left += 1

            while left < right and array[right] not in vowels:
                right -= 1

            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

        return "".join(array)

# Time Complexity: O(3 * n) ==> O(n)
# Space Complexity: O(n)
