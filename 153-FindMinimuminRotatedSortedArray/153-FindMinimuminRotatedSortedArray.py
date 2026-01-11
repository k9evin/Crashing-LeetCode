# Last updated: 1/10/2026, 11:39:22 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        l, r = 0, len(nums) - 1
4
5        if nums[0] <= nums[-1]:
6            return nums[0]
7
8        while l < r:
9            m = l + (r - l) // 2
10            if nums[m] > nums[r]:
11                l = m + 1
12            else:
13                r = m
14
15        return nums[l]
16