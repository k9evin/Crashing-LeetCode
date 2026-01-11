# Last updated: 1/11/2026, 12:04:55 AM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        l, r = 0, len(nums) - 1
4
5        while l <= r:
6            m = l + (r - l) // 2
7            if nums[m] == target:
8                return m
9            if nums[l] <= nums[m]:
10                if nums[l] <= target < nums[m]:
11                    r = m - 1
12                else:
13                    l = m + 1
14            else:
15                if nums[m] < target <= nums[r]:
16                    l = m + 1
17                else:
18                    r = m - 1
19
20        return -1
21