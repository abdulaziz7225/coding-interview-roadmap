from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_altitude = 0
        max_altitude = 0
        for altitude in gain:
            curr_altitude += altitude
            max_altitude = max(max_altitude, curr_altitude)
        return max_altitude

# Time complexity: O(n)
# Space complexity: O(1)
