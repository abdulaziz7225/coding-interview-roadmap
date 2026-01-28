from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = [s]

        for i in range(len(s)):
            if s[i].isdigit():
                continue

            n = len(result)
            for k in range(n):
                permutation = list(result[k])
                permutation[i] = permutation[i].swapcase()
                result.append("".join(permutation))

        return result

# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n)
