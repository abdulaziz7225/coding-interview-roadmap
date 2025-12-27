# Solution 1: Sliding Window
class Solution:
    def checkInclusion(self, pattern: str, string: str) -> bool:
        n = len(string)
        k = len(pattern)

        if k > n:
            return False

        pattern_freq = [0] * 26
        string_freq = [0] * 26

        for i in range(k):
            pattern_freq[ord(pattern[i]) - ord("a")] += 1
            string_freq[ord(string[i]) - ord("a")] += 1

        if string_freq == pattern_freq:
            return True

        for i in range(k, n):
            string_freq[ord(string[i]) - ord("a")] += 1
            string_freq[ord(string[i - k]) - ord("a")] -= 1

            if string_freq == pattern_freq:
                return True

        return False

# n = len(string), k = len(pattern)
# Time Complexity: O(k + 26 * (n - k)) ==> O(n)
# Space Complexity: O(2 * 26) ==> O(1)


# Solution 2: Optimized Sliding Window
class Solution:
    def checkInclusion(self, pattern: str, string: str) -> bool:
        n = len(string)
        k = len(pattern)

        if k > n:
            return False

        pattern_freq = [0] * 26
        string_freq = [0] * 26

        for i in range(k):
            pattern_freq[ord(pattern[i]) - ord("a")] += 1
            string_freq[ord(string[i]) - ord("a")] += 1

        count = 0
        for i in range(26):
            if pattern_freq[i] == string_freq[i]:
                count += 1

        for i in range(k, n):
            left = ord(string[i - k]) - ord("a")
            right = ord(string[i]) - ord("a")

            if count == 26:
                return True

            string_freq[right] += 1
            if string_freq[right] == pattern_freq[right]:
                count += 1
            elif string_freq[right] == pattern_freq[right] + 1:
                count -= 1

            string_freq[left] -= 1
            if string_freq[left] == pattern_freq[left]:
                count += 1
            elif string_freq[left] == pattern_freq[left] - 1:
                count -= 1

        return count == 26

# n = len(string), k = len(pattern)
# Time Complexity: O(k + (n - k)) ==> O(n)
# Space Complexity: O(2 * 26) ==> O(1)
