class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = [0] * 26
        for i in range(len(s)):
            letters[ord(s[i]) - ord('a')] += 1
            letters[ord(t[i]) - ord('a')] -= 1

        for char in letters:
            if char != 0:
                return False
        return True

# n = len(s), k = 26
# Time Complexity: O(n + 2 * k) ==> O(n)
# Space Complexity: O(k) ==> O(1)
