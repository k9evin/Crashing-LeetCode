class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Solution 1:
        # Time complexity: O(m + n)
        # Space complexity: O(n)
        stack = []
        res = []
        dict = {}
        
        for i, n in enumerate(nums2):
            # monotonic decreasing stack, if the curr number is >
            # than the one at the top of the stack, pop it out
            while stack and n > nums2[stack[-1]]:
                idx = stack.pop()
                # record the value and its corresponding next larger value
                dict[nums2[idx]] = n
            stack.append(i)
            
        for j in nums1:
            # find the correspond larger value through dictionary
            res.append(dict.get(j, -1))
        return res
		
		# Solution 2:
        # Time complexity: O()
        # Space complexity: O()
		
		# Solution 3:
        # Time complexity: O()
        # Space complexity: O()