# Last updated: 1/25/2026, 6:38:59 PM
1class Solution:
2    def minimumDifference(self, nums: List[int], k: int) -> int:
3        # 排序数组，使得相近的分数相邻
4        nums.sort()
5
6        # 初始化结果为前 k 个元素的差值
7        res = nums[k - 1] - nums[0]
8
9        # 滑动窗口遍历所有大小为 k 的子数组
10        for i in range(k, len(nums)):
11            # 更新最小差值：当前窗口的最大值 - 最小值
12            res = min(res, nums[i] - nums[i - k + 1])
13
14        return res
15
16
17# Time: O(n log n) - 排序占主导，滑动窗口遍历为 O(n)
18# Space: O(1) - 只使用常数额外空间（原地排序）
19