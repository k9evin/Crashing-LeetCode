# Last updated: 1/4/2026, 1:10:53 PM
1class Solution:
2    def lowerBound(self, nums: List[int], target: int) -> int:
3        l, r = -1, len(nums)  # open interval (l, r)
4        while l + 1 < r:  # while interval not empty
5            m = (l + r) // 2
6            if nums[m] >= target:
7                r = m  # keep m as candidate
8            else:
9                l = m
10        return r  # first index >= target
11
12    def maximumCount(self, nums: List[int]) -> int:
13        neg = self.lowerBound(nums, 0)  # count of nums < 0
14        pos = len(nums) - self.lowerBound(nums, 1)  # count of nums > 0
15        return max(neg, pos)
16
17
18# Time: O(log n) - two binary searches
19# Space: O(1)
20