class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = dict()
        for index, char in enumerate(s):
            last_index[char] = index

        visited = set()
        stack = []
        for index, char in enumerate(s):
            if char in visited:
                continue

            while stack and stack[-1] > char and last_index[stack[-1]] > index:
                visited.remove(stack.pop())

            stack.append(char)
            visited.add(char)

        return "".join(stack)

# n = len(string), c = 26
# Time complexity; O(4 * n) ==> O(n)
# Space complexity: O(3 * c) ==> O(1)
