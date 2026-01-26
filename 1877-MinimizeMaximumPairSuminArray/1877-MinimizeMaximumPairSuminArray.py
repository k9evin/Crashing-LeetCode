# Last updated: 1/25/2026, 7:46:27 PM
1class Solution:
2    def minPairSum(self, nums: List[int]) -> int:
3        nums.sort()
4        max_sum = -1
5
6        l, r = 0, len(nums) - 1
7        while l < r:
8            curr_sum = nums[l] + nums[r]
9            max_sum = max(max_sum, curr_sum)
10            l += 1
11            r -= 1
12
13        return max_sum
14