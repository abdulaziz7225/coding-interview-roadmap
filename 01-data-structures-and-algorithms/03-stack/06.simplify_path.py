class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for p in path.split("/"):
            if p == "..":
                if stack:
                    stack.pop()
            elif p and p != ".":
                stack.append(p)

        return "/" + "/".join(stack)

# Time Complexity: O(3 * n) ==> O(n)
# Space Complexity: O(2 * n) ==> O(n)
