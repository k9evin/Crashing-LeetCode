class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Solution 1:
        # Time complexity: O(m + n)
        # Space complexity: O(n)
#         stack = []    # storing the index
#         res = []
#         dict = {}
        
#         for i, n in enumerate(nums2):
#             # monotonic decreasing stack, if the curr number is >
#             # than the one at the top of the stack, pop it out
#             while stack and n > nums2[stack[-1]]:
#                 idx = stack.pop()
#                 # record the value and its corresponding next larger value
#                 dict[nums2[idx]] = n
#             stack.append(i)
            
#         for j in nums1:
#             # find the correspond larger value through dictionary
#             res.append(dict.get(j, -1))
#         return res
		
		# Solution 2:
        # Time complexity: O(m * n)
        # Space complexity: O(m)
#         dict = {n : i for i, n in enumerate(nums1)}
#         res = [-1] * len(nums1)
        
#         for i in range(len(nums2)):
#             if nums2[i] not in nums1:
#                 continue
#             for j in range(i + 1, len(nums2)):
#                 if nums2[j] > nums2[i]:
#                     idx = dict[nums2[i]]
#                     res[idx] = nums2[j]
#                     break
#         return res
            
		
		# Solution 3:
        # Time complexity: O(m + n)
        # Space complexity: O(m)
        stack = []    # storing the value
        res = [-1] * len(nums1)
        dict = {n : i for i, n in enumerate(nums1)}
        
        for i, n in enumerate(nums2):
            # monotonic decreasing stack, if the curr number is >
            # than the one at the top of the stack, pop it out
            while stack and n > stack[-1]:
                val = stack.pop()
                idx = dict[val]
                res[idx] = n
            if n in nums1:
                stack.append(n)
        return res