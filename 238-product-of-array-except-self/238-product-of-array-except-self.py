class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Solution 1:
        # Time complexity: O(n)
        # Space complexity: O(n)
        # length = len(nums)
        # prefix, suffix = [1] * length, [1] * length
        # answ = []
        # for i in range(1, length):
        #     prefix[i] = nums[i - 1] * prefix[i - 1]
        # for j in range(length - 2, -1, -1):
        #     suffix[j] = nums[j + 1] * suffix[j + 1]
        # for k in range(length):
        #     answ.append(prefix[k] * suffix[k])
        # return answ
		
		# Solution 2:
        # Time complexity: O(n)
        # Space complexity: O(1)
        length = len(nums)
        answ = [1] * length
        left = 1
        for i in range(length):
            answ[i] = left
            left *= nums[i]
        right = 1
        for j in range(length - 1, -1 , -1):
            answ[j] *= right
            right *= nums[j]
        return answ