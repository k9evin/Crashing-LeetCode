# Last updated: 2/14/2026, 6:36:22 PM
1class Solution:
2    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
3        prev_row = [poured]
4
5        for row in range(1, query_row + 1):
6            curr_row = [0] * (row + 1)
7
8            for i in range(row):
9                extra = prev_row[i] - 1
10                if extra > 0:
11                    curr_row[i] += 0.5 * extra
12                    curr_row[i + 1] += 0.5 * extra
13
14            prev_row = curr_row
15
16        return min(1, prev_row[query_glass])
17