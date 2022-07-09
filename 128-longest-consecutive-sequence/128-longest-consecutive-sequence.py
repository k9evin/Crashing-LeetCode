class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Solution 1:
        # Time complexity: O(n) we will visit each number at most twice
        # Space complexity: O(n)
        nums_set = set(nums)
        longest = 0
        for n in nums:
            # 检查 num-1 这个数字是否在 set 中
            # 如果不在则说明这是 sequence 的头
            if (n - 1) not in nums_set:
                length = 0
                # length 增加，如果 num+length 在 set 中
                while (n + length) in nums_set:
                    length += 1
                # 得到一个 sequence 的长度，取最大值
                longest = max(length, longest)
        return longest