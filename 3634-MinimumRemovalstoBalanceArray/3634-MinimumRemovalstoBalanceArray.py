# Last updated: 2/6/2026, 6:04:53 PM
1class Solution:
2    def minRemoval(self, nums: List[int], k: int) -> int:
3        nums.sort()
4        l = 0
5        max_len = 0
6
7        for r in range(len(nums)):
8            while nums[r] > nums[l] * k:
9                l += 1
10            max_len = max(max_len, r - l + 1)
11
12        return len(nums) - max_len
13