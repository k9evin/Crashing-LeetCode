# Last updated: 1/4/2026, 12:41:20 PM
1class Solution:
2    def lowerBound(self, nums: List[int], target: int) -> int:
3        # Open interval (l, r): l = -1, r = len(nums)
4        # Virtual boundaries: nums[-1] = -∞ < target, nums[len(nums)] = +∞ >= target
5        l, r = -1, len(nums)
6
7        # Loop while there's at least one element between l and r
8        # Condition l + 1 < r means interval (l, r) is non-empty
9        while l + 1 < r:
10            m = (
11                l + (r - l) // 2
12            )  # Midpoint calculation (avoids overflow in other languages)
13
14            if nums[m] >= target:
15                r = m  # m is a valid candidate for lower bound, search left half (l, m)
16            else:
17                l = m  # m is too small, search right half (m, r)
18
19        # When loop ends: l + 1 == r
20        # By loop invariant: nums[l] < target and nums[r] >= target
21        # So r is the first index where nums[r] >= target
22        return r
23
24    def searchRange(self, nums: List[int], target: int) -> List[int]:
25        # Find the first position where nums[i] >= target
26        start = self.lowerBound(nums, target)
27
28        # Two failure cases:
29        # 1. start == len(nums): all elements are < target (target too large)
30        # 2. nums[start] != target: first >= target element is actually > target (target missing)
31        # Note: order matters - check bounds before array access to prevent IndexError
32        if start == len(nums) or nums[start] != target:
33            return [-1, -1]
34
35        # Find first position where nums[i] >= target + 1
36        # Since array is sorted, this gives us the position right after the last target
37        # Subtract 1 to get the actual last occurrence of target
38        # Safe to do because we already confirmed target exists
39        end = self.lowerBound(nums, target + 1) - 1
40
41        return [start, end]
42
43
44# Time Complexity: O(log n) - two binary searches, each O(log n)
45# Space Complexity: O(1) - only using constant extra space
46