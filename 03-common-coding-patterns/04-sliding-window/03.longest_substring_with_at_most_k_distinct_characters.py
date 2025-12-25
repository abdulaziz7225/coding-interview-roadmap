class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        count = dict()
        longest_substring = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            while len(count) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

            longest_substring = max(longest_substring, right - left + 1)

        return longest_substring

# Time Complexity: O(2 * n) ==> O(n)
# Space Complexity: O(k)
