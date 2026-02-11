from heapq import heappush, heappop, nlargest
from typing import List


# Solution 1: Sorting
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for num in nums:
            count[num] = count.get(num, 0) + 1

        top_frequent = sorted(count.items(), key=lambda x: x[1], reverse=True)

        result = []
        for i in range(k):
            result.append(top_frequent[i][0])
        return result

# n = len(nums), m = count of unique numbers
# Time Complexity: O(n + m * log(m) + k) ==> O(n + m * log(m))
# In Python, the sort() method sorts a list using the Timsort algorithm which is a combination
# of Merge Sort and Insertion Sort and has O(n) additional space.
# Space Complexity: O(2 * m + k) ==> O(m + k)


# Solution 2: Heap Priority Queue built-in nlargest method
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for num in nums:
            count[num] = count.get(num, 0) + 1

        result = nlargest(k, count.keys(), key=count.get)
        return result

# n = len(nums), m = count of unique numbers
# Time Complexity: O(n + m * log(k) + k) ==> O(n + m * log(m))
# Space Complexity: O(2 * m + k) ==> O(m + k)


# Solution 3: Heap Priority Queue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for num in nums:
            count[num] = count.get(num, 0) + 1

        min_freq_heap = []
        for num, freq in count.items():
            heappush(min_freq_heap, (freq, num))
            if len(min_freq_heap) > k:
                heappop(min_freq_heap)

        result = [num for _, num in min_freq_heap]
        return result

# n = len(nums), m = count of unique numbers
# Time Complexity: O(n + m * log(k) + k) ==> O(n + m * log(m))
# Space Complexity: O(m + 2 * k) ==> O(m + k)
