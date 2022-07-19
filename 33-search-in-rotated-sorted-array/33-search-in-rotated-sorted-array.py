class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Solution 1:
        # Time complexity: O(logn)
        # Space complexity: O(1)
        
        # step 1: find the pivot index
        l = 0
        r = len(nums) - 1
        pivot = -1
        
        while l < r:
            m = (l + r) // 2
            # for example: 7 > 2. We know that the rotation
            # happen in the right half of the array
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
                
        pivot = l
        l = 0
        r = len(nums) - 1
        
        # step 2: figure out which half of the array
        
        # right side
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        # left side
        else:
            r = pivot
            
        # step 3: regular binary search
        while l <= r:
            m = (l + r) // 2
            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                return m
        
        return -1
        
        