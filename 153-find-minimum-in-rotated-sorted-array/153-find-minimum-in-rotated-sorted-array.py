class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Solution 1:
        # Time complexity: O(logn)
        # Space complexity: O(1)
        # edge case: original order
        if nums[0] < nums[-1]:
            return nums[0]
        # find pivot
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]
                