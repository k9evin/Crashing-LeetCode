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
        # Time complexity: O(n)
        # Space complexity: O(1)
        # res = 0
        # l_max = [0] * len(height)
        # r_max = [0] * len(height)
        # for i in range(1, len(height)):
        #     l_max[i] = max(l_max[i - 1], height[i - 1])
        # for j in range(len(height) - 2, -1, -1):
        #     r_max[j] = max(r_max[j + 1], height[j + 1])
        # for k in range(1, len(height) - 1):
        #     trap = min(l_max[k], r_max[k]) - height[k]
        #     if trap > 0:
        #         res += trap
        # return res
		
		# Solution 3:
        # Time complexity: O(n)
        # Space complexity: O(1)
        left, right = 0, len(height) - 1
        l_max, r_max, res = 0, 0, 0
        while left < right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])
            # r_max 是否是右边最大的并不重要，因为能装多少水取决于短边
            if l_max < r_max:
                res += l_max - height[left]
                left += 1
            else:
                res += r_max - height[right]
                right -= 1
        return res