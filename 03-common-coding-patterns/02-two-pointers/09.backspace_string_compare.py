class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ptr1 = len(s) - 1
        ptr2 = len(t) - 1

        while ptr1 >= 0 or ptr2 >= 0:
            ptr1 = self.getNextValidIndex(s, ptr1)
            ptr2 = self.getNextValidIndex(t, ptr2)

            if ptr1 >= 0 and ptr2 >= 0 and s[ptr1] != t[ptr2]:
                return False

            if (ptr1 >= 0) ^ (ptr2 >= 0):
                return False

            ptr1 -= 1
            ptr2 -= 1

        return True

    def getNextValidIndex(self, string: str, index: int) -> int:
        backspace_count = 0

        while index >= 0:
            if string[index] == "#":
                backspace_count += 1
            elif string[index] != "#" and backspace_count > 0:
                backspace_count -= 1
            else:
                break
            index -= 1

        return index

# n = len(s), m = len(t)
# Time Complexity: O(n + m)
# Space Complexity: O(1)
