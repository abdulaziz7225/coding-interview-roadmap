from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []

        for i in range(n - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j - 1] == nums[j]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1

        return result

# Time Complexity: O(n * log(n) + n^2) ==> O(n^2)
# In the worst-case scenario, the number of unique triplets is proportional to the square of the input size
# Space Complexity: O(n + n^2) ==> O(n^2)
