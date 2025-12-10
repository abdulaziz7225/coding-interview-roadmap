# Solution 1: Sorting
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("AEIOUaeiou")
        letters = []

        for char in s:
            if char in vowels:
                letters.append(char)

        letters.sort()

        result = []
        j = 0
        for char in s:
            if char in vowels:
                result.append(letters[j])
                j += 1
            else:
                result.append(char)

        return "".join(result)

# Time complexity: O(3 * n + n * log(n)) ==> O(n * log(n))
# Space complexity: O(3 * n) ==> O(n)


# Solution 2: Counting Sort
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("AEIOUaeiou")
        sorted_vowels = "AEIOUaeiou"
        count = dict()

        for char in s:
            if char in vowels:
                count[char] = count.get(char, 0) + 1

        result = []
        j = 0
        for i, char in enumerate(s):
            if char in vowels:
                while count.get(sorted_vowels[j], 0) == 0:
                    j += 1

                result.append(sorted_vowels[j])
                count[sorted_vowels[j]] -= 1
            else:
                result.append(char)

        return "".join(result)

# k = number of vowels (k = 10)
# Time complexity: O(3 * n) ==> O(n)
# Space complexity: O(n + k) ==> O(n)
