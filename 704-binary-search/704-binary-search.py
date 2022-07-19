class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Solution 1:
        # Time complexity: O(logn)
        # Space complexity: O(1)
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                return mid
        return -1