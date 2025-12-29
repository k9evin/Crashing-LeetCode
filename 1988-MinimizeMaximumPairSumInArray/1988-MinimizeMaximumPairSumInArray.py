# Last updated: 12/29/2025, 1:40:54 AM
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        l, r = 0, len(nums) - 1
        max_sum = 0

        while l < r:
            curr_sum = nums[l] + nums[r]
            max_sum = max(max_sum, curr_sum)
            l += 1
            r -= 1

        return max_sum