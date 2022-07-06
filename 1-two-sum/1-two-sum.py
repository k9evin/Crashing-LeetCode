class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution 1:
        # Time complexity: O(n^2)
        # Space complexity: O(1)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
		
		# Solution 2:
        # Time complexity: O(n)
        # Space complexity: O(n)
        # map the value to the index of the value
        # dict = {}
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in dict:
        #         return [dict[diff], i]
        #     else:
        #         dict[nums[i]] = i
		
		# Solution 3:
        # Time complexity: O()
        # Space complexity: O()
        dict = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dict:
                return [dict[diff], i]
            else:
                dict[n] = i