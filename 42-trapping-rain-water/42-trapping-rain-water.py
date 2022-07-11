class Solution:
    def trap(self, height: List[int]) -> int:
        # Solution 1:
        # Time complexity: O(n^2)
        # Space complexity: O(1)
        # res = 0
        # for i in range(1, len(height)):
        #     l_max, r_max = 0, 0
        #     for j in range(i, len(height)):
        #         r_max = max(r_max, height[j])
        #     for k in range(i, -1, -1):
        #         l_max = max(l_max, height[k])
        #     res += min(l_max, r_max) - height[i]
        # return res
		
		# Solution 2:
        # Time complexity: O()
        # Space complexity: O()
        res = 0
        l_max = [0] * len(height)
        r_max = [0] * len(height)
        for i in range(1, len(height)):
            l_max[i] = max(l_max[i - 1], height[i - 1])
        for j in range(len(height) - 2, -1, -1):
            r_max[j] = max(r_max[j + 1], height[j + 1])
        for k in range(1, len(height) - 1):
            trap = min(l_max[k], r_max[k]) - height[k]
            if trap > 0:
                res += trap
        return res
		
		# Solution 3:
        # Time complexity: O()
        # Space complexity: O()