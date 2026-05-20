from collections import defaultdict
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)

        if n <= 2:
            return n

        ans = 0

        for i in range(n):

            slope_count = defaultdict(int)

            for j in range(i + 1, n):

                x1, y1 = points[i]
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                slope = float('inf') if dx == 0 else dy / dx

                slope_count[slope] += 1

                ans = max(ans, slope_count[slope] + 1)

        return ans
