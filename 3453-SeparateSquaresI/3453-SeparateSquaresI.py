# Last updated: 1/13/2026, 12:10:09 AM
1class Solution:
2    def separateSquares(self, squares: List[List[int]]) -> float:
3        max_y = 0
4        total_area = 0
5
6        for x, y, l in squares:
7            max_y = max(max_y, y + l)
8            total_area += l**2
9
10        def curr_area(y_limit):
11            area = 0
12
13            for x, y, l in squares:
14                if y < y_limit:
15                    area += l * min(l, y_limit - y)
16
17            return area
18
19        lo, hi = 0, max_y
20        diff = 1e-5
21
22        while abs(hi - lo) > diff:
23            mid = lo + (hi - lo) / 2
24            if curr_area(mid) >= total_area / 2:
25                hi = mid
26            else:
27                lo = mid
28
29        return hi
30