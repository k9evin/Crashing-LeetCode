# Last updated: 12/29/2025, 1:40:07 AM
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0, len(nums), 3):
            if nums[i] + k >= nums[i+2]:
                ans.append(nums[i:i+3])
            else:
                return []
        return ans