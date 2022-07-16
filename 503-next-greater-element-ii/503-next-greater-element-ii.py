class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Solution 1:
        # Time complexity: O(n)
        # Space complexity: O(n)
        n = len(nums)
        stack = []
        res = [-1] * n
        val = 0
        
        for i in range(n * 2):
            num = nums[i % n]
            # monotonic decreasing stack (storing index)
            while stack and num > nums[stack[-1]]:
                idx = stack.pop()
                res[idx] = num
            stack.append(i % n)
        return res

		# Solution 2:
        # Time complexity: O()
        # Space complexity: O()
		
		# Solution 3:
        # Time complexity: O()
        # Space complexity: O()