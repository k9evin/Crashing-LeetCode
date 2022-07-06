class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 1. Brute force solution:
        # Time complexity: O(n^2)
        # Space complexity: O(1)
        # for i in range(0, len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True;
        # return False;
        
        # 2. Order the list:
        # Time complexity: O(n^2)
        # Space complexity: O(1)
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
            