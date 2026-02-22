# Last updated: 2/22/2026, 5:43:19 PM
1class Solution:
2    def binaryGap(self, n: int) -> int:
3        n //= n & -n
4        if n == 1:
5            return 0
6
7        max_gap = 0
8        gap = 0
9
10        while n:
11            if n & 1:
12                max_gap = max(max_gap, gap)
13                gap = 0
14            else:
15                gap += 1
16            n >>= 1
17
18        return max_gap + 1
19