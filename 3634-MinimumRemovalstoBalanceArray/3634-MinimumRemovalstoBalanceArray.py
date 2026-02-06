# Last updated: 2/6/2026, 6:12:11 PM
1class Solution:
2    def minRemoval(self, nums: List[int], k: int) -> int:
3        # 1. 排序：将问题转化为寻找最长连续子数组
4        nums.sort()
5        l = 0           # 滑动窗口左指针
6        max_len = 0     # 记录满足条件的最大窗口长度
7
8        # 2. 滑动窗口：右指针遍历整个数组
9        for r in range(len(nums)):
10            # 3. 当窗口不满足平衡条件时，收缩左边界
11            # 条件：max <= min * k，即 nums[r] <= nums[l] * k
12            # 不满足时，增大最小值（l右移）以恢复条件
13            while nums[r] > nums[l] * k:
14                l += 1
15
16            # 4. 更新最大窗口长度
17            max_len = max(max_len, r - l + 1)
18
19        # 5. 最小删除次数 = 总长度 - 最长有效子数组长度
20        return len(nums) - max_len
21
22# 时间复杂度：O(n log n) - 排序 O(n log n) + 滑动窗口 O(n)
23# 空间复杂度：O(log n) 或 O(n) - 取决于排序算法的空间复杂度
24