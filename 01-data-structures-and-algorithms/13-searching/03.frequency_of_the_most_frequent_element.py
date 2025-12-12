from typing import List


# Solution 1: Sliding Window
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 0
        curr = 0
        left = 0

        for right in range(len(nums)):
            target = nums[right]
            curr += target

            while (right - left + 1) * target - curr > k:
                curr -= nums[left]
                left += 1

            result = max(result, right - left + 1)

        return result

# Time Complexity: O(n * log(n) + 2 * n) ==> O(n * log(n))
# In Python, the sort() method sorts a list using the Timsort algorithm which is a combination
# of Merge Sort and Insertion Sort and has O(n) additional space.
# Space Complexity: O(n)


# Solution 2: Advanced Sliding Window
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr = 0
        left = 0

        for right in range(len(nums)):
            target = nums[right]
            curr += target

            if (right - left + 1) * target - curr > k:
                curr -= nums[left]
                left += 1

        return len(nums) - left

# Time Complexity: O(n * log(n) + 2 * n) ==> O(n * log(n))
# In Python, the sort() method sorts a list using the Timsort algorithm which is a combination
# of Merge Sort and Insertion Sort and has O(n) additional space.
# Space Complexity: O(n)


# Solution 3: Binary Search
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        prefix = []
        cum_sum = 0
        for num in nums:
            cum_sum += num
            prefix.append(cum_sum)

        result = 0
        for idx in range(len(nums)):
            result = max(result, self.check(nums, prefix, idx, k))

        return result

    def check(self, array: List[int], prefix: List[int], idx: int, k: int) -> int:
        left = 0
        right = idx
        target = array[idx]
        best = idx

        while left <= right:
            middle = (left + right) // 2
            count = idx - middle + 1

            final_sum = count * target
            original_sum = prefix[idx] - prefix[middle] + array[middle]
            operations_required = final_sum - original_sum

            if operations_required > k:
                left = middle + 1
            else:
                best = middle
                right = middle - 1

        return idx - best + 1

# Time Complexity: O(2 * n * log(n) + n) ==> O(n * log(n))
# In Python, the sort() method sorts a list using the Timsort algorithm which is a combination
# of Merge Sort and Insertion Sort and has O(n) additional space.
# Space Complexity: O(2 * n) ==> O(n)
