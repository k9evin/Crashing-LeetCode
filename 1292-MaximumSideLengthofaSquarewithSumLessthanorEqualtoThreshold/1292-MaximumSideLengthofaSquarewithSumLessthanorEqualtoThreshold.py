# Last updated: 1/19/2026, 6:41:14 PM
1class Solution:
2    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
3        m, n = len(mat), len(mat[0])
4        P = [[0] * (n + 1) for _ in range(m + 1)]
5        for i in range(1, m + 1):
6            for j in range(1, n + 1):
7                P[i][j] = (
8                    P[i - 1][j]
9                    + P[i][j - 1]
10                    - P[i - 1][j - 1]
11                    + mat[i - 1][j - 1]
12                )
13
14        def getRect(x1, y1, x2, y2):
15            return P[x2][y2] - P[x1 - 1][y2] - P[x2][y1 - 1] + P[x1 - 1][y1 - 1]
16
17        r, ans = min(m, n), 0
18        for i in range(1, m + 1):
19            for j in range(1, n + 1):
20                for c in range(ans + 1, r + 1):
21                    if (
22                        i + c - 1 <= m
23                        and j + c - 1 <= n
24                        and getRect(i, j, i + c - 1, j + c - 1) <= threshold
25                    ):
26                        ans += 1
27                    else:
28                        break
29        return ans