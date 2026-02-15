from typing import List
from heapq import heapify, heappop


# Solution 1: Sorting
class Solution:
    def findLeastNumOfUniqueInts(self, nums: List[int], k: int) -> int:
        count = dict()
        for num in nums:
            count[num] = count.get(num, 0) + 1

        frequencies = sorted(count.values(), reverse=True)

        while k > 0 and frequencies[-1] <= k:
            freq = frequencies.pop()
            k -= freq

        return len(frequencies)

# n = len(nums), m = count of unique numbers
# Time Complexity: O(n + m + 2 * m * log(m)) ==> O(n + m * log(m))
# Space Complexity: O(2 * m) ==> O(m)


# Solution 2: Min Heap
class Solution:
    def findLeastNumOfUniqueInts(self, nums: List[int], k: int) -> int:
        count = dict()
        for num in nums:
            count[num] = count.get(num, 0) + 1

        frequencies = list(count.values())
        heapify(frequencies)

        while k > 0 and frequencies[0] <= k:
            freq = heappop(frequencies)
            k -= freq

        return len(frequencies)

# n = len(nums), m = count of unique numbers
# Time Complexity: O(n + 2 * m + m * log(m)) ==> O(n + m * log(m))
# Space Complexity: O(2 * m) ==> O(m)


# Solution 3: Counting Sort
class Solution:
    def findLeastNumOfUniqueInts(self, nums: List[int], k: int) -> int:
        count = dict()
        for num in nums:
            count[num] = count.get(num, 0) + 1

        n = len(nums)

        count_of_frequencies = [0] * (n + 1)
        for freq in count.values():
            count_of_frequencies[freq] += 1

        remaining_unique_elements = len(count)
        for index in range(1, n + 1):
            num_of_elements = min(k // index, count_of_frequencies[index])
            k -= index * (num_of_elements)

            remaining_unique_elements -= num_of_elements

            if k < index:
                return remaining_unique_elements

        return 0

# n = len(nums), m = count of unique numbers
# Time Complexity: O(3 * n + m) ==> O(n)
# Space Complexity: O(n + m) ==> O(n)
