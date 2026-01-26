# Last updated: 1/25/2026, 7:53:03 PM
1class Solution:
2    def minPairSum(self, nums: List[int]) -> int:
3        # 1. 先排序数组 - 关键步骤：排序后可以按最优策略配对
4        nums.sort()
5
6        # 2. 初始化最大对和
7        max_sum = -1
8
9        # 3. 双指针：一个指向最小元素，一个指向最大元素
10        l, r = 0, len(nums) - 1
11
12        # 4. 遍历数组，将最小和最大的元素配对
13        while l < r:
14            # 计算当前配对的和
15            curr_sum = nums[l] + nums[r]
16
17            # 更新最大对和
18            max_sum = max(max_sum, curr_sum)
19
20            # 移动指针：左指针向右，右指针向左
21            l += 1
22            r -= 1
23
24        # 5. 返回最小化的最大对和
25        return max_sum
26
27
28# 时间复杂度：O(n log n)
29# - 排序操作：O(n log n)  （Python的Timsort算法）
30# - 双指针遍历：O(n)
31# - 总时间复杂度：O(n log n)
32
33# 空间复杂度：O(1)（不考虑排序所需的额外空间）
34