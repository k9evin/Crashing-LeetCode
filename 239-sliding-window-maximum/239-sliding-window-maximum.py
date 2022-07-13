class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Solution 1:
        # Time complexity: O(n)
        # Space complexity: O(1)
        l = 0
        res = []
        d = collections.deque()
        
        for r in range(len(nums)):
            while d and nums[d[-1]] < nums[r]:
                d.pop()
            d.append(r)
            if d[0] < l:
                d.popleft()
            if (r + 1) >= k:
                res.append(nums[d[0]])
                l += 1
        return res 
		
		# Solution 2:
        # Time complexity: O()
        # Space complexity: O()
		
		# Solution 3:
        # Time complexity: O()
        # Space complexity: O()