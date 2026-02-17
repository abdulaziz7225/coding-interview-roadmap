from heapq import heappush, heappop
from collections import deque


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        count = dict()
        for char in s:
            count[char] = count.get(char, 0) + 1

        max_heap = []
        for char, freq in count.items():
            heappush(max_heap, (-freq, char))

        result = []
        queue = deque()

        while max_heap:
            curr_freq, curr_char = heappop(max_heap)
            result.append(curr_char)
            queue.append((curr_freq + 1, curr_char))

            if len(queue) >= k:
                cooled_freq, cooled_char = queue.popleft()
                if cooled_freq < 0:
                    heappush(max_heap, (cooled_freq, cooled_char))

        if len(result) != len(s):
            return ""
        return "".join(result)

# n = len(s), m = number of unique characters
# Time Complexity: O(n + (n + m) * log(m)) ==> O(n * log(m))
# Space Complexity: O(n + 3 * m) ==> O(n)
