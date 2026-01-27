from typing import List
from collections import deque


# Solution 1
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        queue = deque(nums)
        return self.backtrack(queue)
    
    def backtrack(self, queue: deque) -> List[List[int]]:
        if len(queue) == 1:
            return [list(queue)]
        
        result = []

        for _ in range(len(queue)):
            curr = queue.popleft()
            permutations = self.backtrack(queue)

            for perm in permutations:
                perm.append(curr)

            result.extend(permutations)
            queue.append(curr)

        return result
    
# Time Complexity: O(n * n!)
# Space Complexity: O(n * n!)

# Solution 2
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.backtrack(0, nums)
        return self.result

    def backtrack(self, start: int, nums: List[int]) -> None:
        if start == len(nums):
            self.result.append(nums.copy())
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            self.backtrack(start + 1, nums)
            nums[start], nums[i] = nums[i], nums[start]

# Time Complexity: O(n * n!)
# Space Complexity: O(n * n!)
