class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Solution 1:
        # Time complexity: O(n^2)
        # Space complexity: O(n)
        # res = [0] * len(temperatures)
        # for l in range(len(temperatures)):
        #     for r in range(l + 1, len(temperatures)):
        #         if temperatures[r] > temperatures[l]:
        #             res[l] = r - l
        #             break
        # return res
    
		# Solution 2:
        # Time complexity: O(n)
        # Space complexity: O(n)
        stack = []
        n = len(temperatures)
        res = [0] * n
        
        # monotonic decreasing stack
        for r in range(n):
            # compare the current element with the top 
            # element in the stack
            while stack and temperatures[r] > temperatures[stack[-1]]:
                # the index of the top element
                l = stack.pop()
                # number of days to wait
                res[l] = r - l
            # once we've compared the prev element, append the curr
            # element to the stack
            stack.append(r)
        return res