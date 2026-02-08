from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image[0])
        for row in image:
            for i in range((n + 1) // 2):
                row[i], row[n - i - 1] = (row[n - i - 1] ^ 1), (row[i] ^ 1)
        return image

# Time Complexity: O(n^2)
# Space Complexity: O(1)
