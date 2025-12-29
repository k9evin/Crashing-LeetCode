# Last updated: 12/29/2025, 1:40:52 AM
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        # steps to reach the smallest number
        step = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                step += 1
            res += step
        return res