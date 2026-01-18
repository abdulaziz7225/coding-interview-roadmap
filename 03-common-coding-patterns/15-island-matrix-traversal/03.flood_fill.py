from typing import List


# Solution: Iterative Depth-First Search with in-place modification
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initial_color = image[sr][sc]
        if initial_color == color:
            return image

        stack = [(sr, sc)]
        image[sr][sc] = color

        while stack:
            row, col = stack.pop()
            directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == initial_color:
                    image[r][c] = color
                    stack.append((r, c))

        return image

# n = len(rows), m = len(cols)
# Time Complexity: O(n * m)
# Space Complexity: O(1)
