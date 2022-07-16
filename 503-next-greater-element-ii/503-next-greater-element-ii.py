class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Solution 1:
        # Time complexity: O(n)
        # Space complexity: O(n)
        n = len(nums)
        stack = []
        res = [-1] * n
        val = 0
        
        # 用 n * 2 将数组长度翻倍，再用 i % n 来代表index
        for i in range(n * 2):
            num = nums[i % n]
            # monotonic decreasing stack (storing index)
            while stack and num > nums[stack[-1]]:
                idx = stack.pop()
                res[idx] = num
            # append the index of the number, so later when we pop
            # we know the corresponded result index
            stack.append(i % n)
        return res