# Last updated: 1/16/2026, 2:41:18 AM
1class Solution:
2    def maximizeSquareArea(
3        self, m: int, n: int, hFences: List[int], vFences: List[int]
4    ) -> int:
5        MOD = 10**9 + 7
6
7        def getAllGaps(fences, end):
8            # Add the boundaries (top-left corner at 1 and bottom-right corner at end)
9            fences.append(1)
10            fences.append(end)
11            fences.sort()
12
13            gaps = set()
14
15            # Calculate all possible gaps between any two fences
16            # This represents all possible side lengths after removing fences
17            for i in range(len(fences)):
18                for j in range(i + 1, len(fences)):
19                    gaps.add(fences[j] - fences[i])
20
21            return gaps
22
23        # Get all possible horizontal side lengths (gaps between horizontal fences)
24        hgaps = getAllGaps(hFences, m)
25
26        # Get all possible vertical side lengths (gaps between vertical fences)
27        vgaps = getAllGaps(vFences, n)
28
29        # Find common gaps - these are valid square side lengths
30        # (a square needs equal horizontal and vertical dimensions)
31        shared_gaps = hgaps.intersection(vgaps)
32
33        # If no common gaps exist, we cannot form a square
34        if not shared_gaps:
35            return -1
36
37        # Find the maximum possible square side length
38        max_shared_gaps = max(shared_gaps)
39
40        # Return the area of the maximum square modulo 10^9 + 7
41        return max_shared_gaps**2 % MOD
42
43
44# Time Complexity: O(h^2 + v^2) where h = len(hFences), v = len(vFences)
45# Space Complexity: O(h^2 + v^2) for storing gap sets
46