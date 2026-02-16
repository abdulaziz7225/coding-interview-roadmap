from heapq import heappush, heappop


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = dict()
        for char in s:
            count[char] = count.get(char, 0) + 1

        max_heap = []
        for char, freq in count.items():
            heappush(max_heap, (-freq, char))

        prev_char = ""
        prev_freq = 0
        result = []

        while max_heap:
            freq, char = heappop(max_heap)
            result.append(char)
            if prev_freq < 0:
                heappush(max_heap, (prev_freq, prev_char))

            freq += 1
            prev_char = char
            prev_freq = freq

        if len(result) != len(s):
            return ""
        return "".join(result)

# Time Complexity: O(2 * n * log(n) + 2 * n) ==> O(n * log(n))
# Space Complexity: O(4 * n) ==> O(n)
