# Last updated: 1/25/2026, 6:38:00 PM
1class Solution:
2    def minimumDifference(self, nums: List[int], k: int) -> int:
3        nums.sort()
4
5        res = nums[k - 1] - nums[0]
6
7        for i in range(k, len(nums)):
8            res = min(res, nums[i] - nums[i - k + 1])
9
10        return res
11