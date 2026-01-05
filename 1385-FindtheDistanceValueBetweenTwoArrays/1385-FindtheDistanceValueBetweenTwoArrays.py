# Last updated: 1/4/2026, 7:43:04 PM
1class Solution:
2    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
3        # [4,5,8] [1,8,9,10]
4        arr2.sort()
5        count = 0
6
7        for x in arr1:
8            start = x - d
9            end = x + d
10
11            # We use open interval binary search (l, r) to find the first element >= start
12            # Initial boundaries: l = -1 (all indices > l), r = len(arr2) (all indices < r)
13            l, r = -1, len(arr2)
14            while l + 1 < r:
15                m = l + (r - l) // 2
16                if arr2[m] >= start:
17                    r = m  # arr2[m] is a candidate for being the first >= start, keep it in range
18                else:
19                    l = m  # arr2[m] is too small, exclude it by moving left boundary
20
21            # After the loop, r is the smallest index such that arr2[r] >= start
22            # This is equivalent to bisect_left(arr2, start)
23            # Now check if this candidate is within the forbidden range [start, end]
24            # If r is out of bounds, all elements in arr2 are < start → safe
25            # If arr2[r] > end, then the first element >= start is already beyond end → safe
26            if r >= len(arr2) or arr2[r] > end:
27                count += 1  # x is valid: no element in arr2 is within distance d
28
29        return count
30
31
32# Time Complexity: O(m log n) where m = len(arr1), n = len(arr2)
33#   - Sorting arr2 takes O(n log n)
34#   - For each of m elements in arr1, we perform a binary search in arr2 (O(log n))
35#   - Total: O(n log n + m log n) = O((m + n) log n), but since constraints allow up to 500 elements,
36#     and typically m, n are comparable, we simplify to O(m log n) as dominant term when m ≥ n
37# Space Complexity: O(1) extra space (sorting is in-place, only using constant extra variables)
38