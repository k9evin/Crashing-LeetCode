# Last updated: 12/29/2025, 2:29:15 AM
1# The isBadVersion API is already defined for you.
2# def isBadVersion(version: int) -> bool:
3
4
5class Solution:
6    def firstBadVersion(self, n: int) -> int:
7        l, r = 1, n  # Using left-closed right-open interval [1, n)
8
9        # Loop condition l < r maintains the half-open interval invariant
10        while l < r:
11            m = l + (r - l) // 2  # Prevents potential overflow
12
13            if isBadVersion(m):
14                # m is bad, so first bad version is at m or to the left
15                # Keep m in search space by setting r = m
16                r = m
17            else:
18                # m is good, so first bad version must be to the right
19                # Exclude m by setting l = m + 1
20                l = m + 1
21
22        # When loop exits, l == r and points to first bad version
23        return l
24
25
26# Time Complexity: O(log n)
27# - Binary search reduces search space by half each iteration
28
29# Space Complexity: O(1)
30# - Only using constant extra space for pointers l, r, m
31