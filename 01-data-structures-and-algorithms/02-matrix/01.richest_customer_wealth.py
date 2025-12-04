from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for account in accounts:
            richest = max(richest, sum(account))
        return richest

# Time Complexity: O(m * n)
# Space Complexity: O(1)
