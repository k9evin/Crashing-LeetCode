# Last updated: 12/29/2025, 1:56:55 AM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        l, r = 0, len(nums) - 1
4
5        while l <= r:
6            m = l + (r - l) // 2
7            if nums[m] < target:
8                l = m + 1
9            elif nums[m] > target:
10                r = m - 1
11            else:
12                return m
13
14        return -1
15