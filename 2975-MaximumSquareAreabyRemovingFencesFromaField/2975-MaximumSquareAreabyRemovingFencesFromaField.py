# Last updated: 1/16/2026, 2:34:49 AM
1class Solution:
2    def maximizeSquareArea(
3        self, m: int, n: int, hFences: List[int], vFences: List[int]
4    ) -> int:
5        MOD = 10**9 + 7
6        def getAllGaps(fences, end):
7            fences.append(1)
8            fences.append(end)
9            fences.sort()
10
11            gaps = set()
12
13            for i in range(len(fences)):
14                for j in range(i + 1, len(fences)):
15                    gaps.add(fences[j] - fences[i])
16
17            return gaps
18
19        hgaps = getAllGaps(hFences, m)
20        vgaps = getAllGaps(vFences, n)
21
22        shared_gaps = hgaps.intersection(vgaps)
23
24        if not shared_gaps:
25            return -1
26
27        max_shared_gaps = max(shared_gaps)
28
29        return max_shared_gaps ** 2 % MOD
30