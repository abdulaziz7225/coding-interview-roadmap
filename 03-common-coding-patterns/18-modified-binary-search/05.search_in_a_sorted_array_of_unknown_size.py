# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# class ArrayReader:
#     def get(self, index: int) -> int:


class Solution:
    def search(self, reader: "ArrayReader", target: int) -> int:
        left = 0
        right = 1

        while reader.get(right) < target:
            left = right
            right *= 2

        return self.binary_search(reader, left, right, target)

    def binary_search(self, reader: "ArrayReader", left: int, right: int, target: int) -> int:
        while left <= right:
            middle = (left + right) // 2
            candidate = reader.get(middle)
            if candidate == target:
                return middle
            elif candidate < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1

# Time Complexity: O(log(n))
# Space Complexity: O(1)
