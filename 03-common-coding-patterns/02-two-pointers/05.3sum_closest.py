from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        result = float("inf")

        for i in range(n - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == target:
                    return total
                elif abs(total - target) < abs(result - target):
                    result = total
                elif total < target:
                    j += 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1
                else:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return result

# Time Complexity: O(n * log(n) + n^2) ==> O(n^2)
# In Python, the sort() method sorts a list using the Timsort algorithm and has O(n) additional space.
# Space Complexity: O(n)
