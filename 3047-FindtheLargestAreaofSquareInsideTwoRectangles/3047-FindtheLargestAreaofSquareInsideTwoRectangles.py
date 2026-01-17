# Last updated: 1/17/2026, 6:56:39 PM
1class Solution:
2    def largestSquareArea(
3        self, bottomLeft: List[List[int]], topRight: List[List[int]]
4    ) -> int:
5        side = 0
6        n = len(bottomLeft)
7
8        for i in range(n):
9            for j in range(i + 1, n):
10                min_x = max(bottomLeft[i][0], bottomLeft[j][0])
11                max_x = min(topRight[i][0], topRight[j][0])
12                min_y = max(bottomLeft[i][1], bottomLeft[j][1])
13                max_y = min(topRight[i][1], topRight[j][1])
14
15                if min_x < max_x and min_y < max_y:
16                    curr_side = min(max_x - min_x, max_y - min_y)
17                    side = max(side, curr_side)
18
19        return side**2
20