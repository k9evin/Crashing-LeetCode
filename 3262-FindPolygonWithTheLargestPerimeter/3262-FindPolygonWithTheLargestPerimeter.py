# Last updated: 12/29/2025, 1:40:09 AM
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        previous_elements_sum = 0
        ans = -1
        for num in nums:
            if num < previous_elements_sum:
                ans = num + previous_elements_sum
            previous_elements_sum += num
        return ans