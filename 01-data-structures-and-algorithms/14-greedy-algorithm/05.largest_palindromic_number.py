class Solution:
    def largestPalindromic(self, num: str) -> str:
        count = [0] * 10
        for digit in num:
            count[int(digit)] += 1

        first_half = []

        # 1. Process digits 9 down to 0
        for digit in range(9, -1, -1):
            if digit == 0 and not first_half:
                continue

            pairs = count[digit] // 2
            if pairs > 0:
                first_half.append(str(digit) * pairs)

        # 2. Determine Middle: The largest digit with an odd count
        middle = ""
        for digit in range(9, -1, -1):
            if count[digit] % 2 == 1:
                middle = str(digit)
                break

        if not first_half and not middle:
            return "0"

        return "".join(first_half) + middle + "".join(first_half[::-1])

# n = len(num)
# Time Complexity: O(3 * n) => O(n)
# Space Complexity: O(n)
