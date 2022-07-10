class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Solution 1:
        # Time complexity: O(nlogn) + O(n^2) = O(n^2)
        # Space complexity: O(1) depends on the sorting algorithm
        answ = []
        nums.sort()
        
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            if n > 0:
                break
            left, right = i + 1, len(nums) - 1
            while left < right:
                result = n + nums[left] + nums[right]
                if result > 0:
                    right -= 1
                elif result < 0:
                    left += 1
                else:
                    answ.append([n, nums[left], nums[right]])
                    # here we found a valid solution, but it doesn't mean
                    # there aren't any other combination with n
                    left += 1
                    while (left < right and 
                           nums[left] == nums[left - 1]):
                        left += 1
        return answ
            
		
		# Solution 2:
        # Time complexity: O()
        # Space complexity: O()
		
		# Solution 3:
        # Time complexity: O()
        # Space complexity: O()