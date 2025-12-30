from typing import List


class Solution:
    def findFirstKthPositive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        i = 0
        result = []

        while i < n:
            j = nums[i] - 1
            if 0 <= j < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        seen = set()

        for i in range(n):
            if len(result) == k:
                return result
            if nums[i] != i + 1:
                result.append(i + 1)
                seen.add(nums[i])

        l = n + 1
        while len(result) < k:
            if l not in seen:
                result.append(l)
            l += 1

        return result

# Time Complexity: O(3 * n - 1 + k) ==> O(n + k)
# Space Complexity: O(k)
