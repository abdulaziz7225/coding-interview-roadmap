# Solution 1: Binary Search
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x

        while left <= right:
            middle = (left + right) // 2
            square = middle ** 2
            if square == x:
                return middle
            elif square < x:
                left = middle + 1
            else:
                right = middle - 1

        # Alternatively: return left - 1
        return right

# Time Complexity: O(log(n))
# Space Complexity: O(1)


# Solution 2: Newton's method
class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while r ** 2 > x:
            r = (r ** 2 + x) // (2 * r)
        return r

# Time Complexity: O(log(n))
# Space Complexity: O(1)
