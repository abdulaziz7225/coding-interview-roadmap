from heapq import heappush, heappop


# Solution 1: Sorting
class Solution:
    def frequencySort(self, string: str) -> str:
        result = []
        count = dict()

        for char in string:
            count[char] = count.get(char, 0) + 1

        sorted_pairs = sorted(
            count.items(), key=lambda x: x[1], reverse=True)
        for char, freq in sorted_pairs:
            result.append(char * freq)

        return "".join(result)

# m is the number of unique characters
# Time Complexity: O(2 * n + m * log(m)) ==> O(n + m * log(m))
# Space Complexity: O(n + 2 * m) ==> O(n + m)


# Solution 2: Heap Priority Queue
class Solution:
    def frequencySort(self, string: str) -> str:
        result = []
        count = dict()

        for char in string:
            count[char] = count.get(char, 0) + 1

        max_heap = []
        for char, freq in count.items():
            heappush(max_heap, [-freq, char])

        while max_heap:
            freq, char = heappop(max_heap)
            result.append(char * -freq)

        return "".join(result)

# m is the number of unique characters
# Time Complexity: O(2 * n + 2 * m * log(m)) ==> O(n + m * log(m))
# Space Complexity: O(n + 2 * m) ==> O(n + m)


# Solution 3: Bucket Sort
class Solution:
    def frequencySort(self, string: str) -> str:
        result = []
        count = dict()
        for char in string:
            count[char] = count.get(char, 0) + 1

        max_freq = max(count.values())
        freq_bucket = [[] for _ in range(max_freq + 1)]

        for char, freq in count.items():
            freq_bucket[freq].append(char)

        for freq in range(max_freq, -1, -1):
            for char in freq_bucket[freq]:
                result.append(char * freq)

        return "".join(result)

# m is the number of unique characters
# Time Complexity: O(2 * (n + m) + max_freq) ==> O(n + m)
# Space Complexity: O(2 * n + m) ==> O(n + m)
