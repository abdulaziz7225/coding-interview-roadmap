class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        low = uniqueCnt1 + uniqueCnt2
        high = divisor1 * divisor2 * uniqueCnt1 * uniqueCnt2
        lcm = self.get_lcm(divisor1, divisor2)

        while low < high:
            middle = (low + high) // 2
            count_both = middle // lcm

            if (middle - count_both >= uniqueCnt1 + uniqueCnt2) and \
                (middle - (middle // divisor1) >= uniqueCnt1) and \
                    (middle - (middle // divisor2) >= uniqueCnt2):
                high = middle
            else:
                low = middle + 1

        return low

    def get_gcd(self, a: int, b: int) -> int:
        """
        Find Greatest Common Divisor
        """
        while b:
            a, b = b, a % b
        return a

    def get_lcm(self, a: int, b: int) -> int:
        """
        Find Least Common Multiple
        """
        if a == 0 or b == 0:
            return 0

        return abs(a * b) // self.get_gcd(a, b)


# low = uniqueCnt1 + uniqueCnt2
# high = divisor1 * divisor2 * uniqueCnt1 * uniqueCnt2
# Time Complexity: O(log(high - min))
# Space Complexity: O(1)
