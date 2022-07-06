class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Solution 1:
        # Time complexity: O(n^2)
        # Space complexity: O(1)
        # for i in range(0, len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True;
        # return False;
        
        # Solution 2:
        # Time complexity: O(nlogn)
        # Space complexity: O(1)
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         return True
        # return False
        
        # Solution 3:
        # Time complexity: O()
        # Space complexity: O()
        hashset = set()        
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
        
            