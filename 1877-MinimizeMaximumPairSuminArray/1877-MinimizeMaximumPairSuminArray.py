# Last updated: 1/24/2026, 6:42:35 PM
1class Solution:
2    def minPairSum(self, nums: List[int]) -> int:
3        nums.sort()
4        
5        l, r = 0, len(nums) - 1
6        max_sum = 0
7
8        while l < r:
9            curr_sum = nums[l] + nums[r]
10            max_sum = max(max_sum, curr_sum)
11            l += 1
12            r -= 1
13
14        return max_sum