from heapq import heappush, heappop, heappushpop


# Solution 1
class MedianFinder:

    def __init__(self):
        self.max_heap = []  # First element is the smallest. Elements are stored with negative sign
        self.min_heap = []  # First element is the greatest

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == len(self.max_heap):
            heappush(self.max_heap, -heappushpop(self.min_heap, -num))
        else:
            heappush(self.min_heap, -heappushpop(self.max_heap, num))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.max_heap[0] - self.min_heap[0]) / 2
        return self.max_heap[0]

# n = len(nums)
# Time Complexity:
# addNum(): O(3 * log(n)) ==> O(log(n))
# findMedian(): O(1)
# Space Complexity: O(n)


# Solution 2
class MedianFinder:

    def __init__(self):
        self.max_heap = []  # First element is the smallest. Elements are stored with negative sign
        self.min_heap = []  # First element is the greatest

    def addNum(self, num: int) -> None:
        heappush(self.min_heap, num)
        heappush(self.max_heap, -heappop(self.min_heap))
        if len(self.max_heap) > len(self.min_heap):
            heappush(self.min_heap, -heappop(self.max_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        return self.min_heap[0]

# n = len(nums)
# Time Complexity:
# addNum(): O(5 * log(n)) ==> O(log(n))
# findMedian(): O(1)
# Space Complexity: O(n)
