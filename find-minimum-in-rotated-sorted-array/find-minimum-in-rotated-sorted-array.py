class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        if nums[0] < nums[-1]:
            return nums[0]

        while left < right:
            mid = (left + right) // 2
            # check the right number to avoid edge case (sorted list)
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # include the mid number because nums[mid] <= nums[right]
                right = mid
        # at his point, we find the minimum sorted portion, which is the 
        # left-most one
        return nums[left]
    # O(logn), O(1) 
