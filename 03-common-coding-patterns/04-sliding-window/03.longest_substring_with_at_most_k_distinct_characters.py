class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        count = dict()

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            if len(count) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

        return right - left + 1

# Time Complexity: O(n)
# Space Complexity: O(k)
