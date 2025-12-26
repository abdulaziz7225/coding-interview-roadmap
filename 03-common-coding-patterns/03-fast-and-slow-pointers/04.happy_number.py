# Solution 1: Hash Set
class Solution:
    def isHappy(self, n: int) -> bool:
        seen_nums = {n}

        while n != 1:
            curr_sum = 0
            while n > 0:
                n, r = divmod(n, 10)
                curr_sum += r ** 2

            if curr_sum in seen_nums:
                return False

            seen_nums.add(curr_sum)
            n = curr_sum

        return True

# k is the number of unique numbers encountered and stored in the set before a cycle is detected or the number 1 is found
# Since O(k) is a small constant, the time complexity can be simplified from O(k * log(n)) to O(log(n)).
# Time Complexity: O(k * log(n)) ==> O(log(n))
# Space Complexity: O(k)


# Solution 2: Two Pointers
class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate_next(n: int) -> int:
            output = 0
            while n > 0:
                n, r = divmod(n, 10)
                output += r**2
            return output

        slow = calculate_next(n)
        fast = calculate_next(calculate_next(n))

        while slow != fast:
            if fast == 1:
                return True
            slow = calculate_next(slow)
            fast = calculate_next(calculate_next(fast))

        return slow == 1

# Time Complexity: O(k * log(n)) ==> O(log(n))
# Space Complexity: O(1)
