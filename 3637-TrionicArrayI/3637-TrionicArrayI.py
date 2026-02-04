# Last updated: 2/3/2026, 7:14:37 PM
1class Solution:
2    def isTrionic(self, nums: List[int]) -> bool:
3        count = 1  # 段数计数器，初始为1（第一段递增）
4        is_increasing = True  # 当前段是否为递增，初始为True
5        p = -1  # 第一个转折点（递增→递减）
6        q = -1  # 第二个转折点（递减→递增）
7
8        for i in range(1, len(nums)):
9            if nums[i - 1] < nums[i]:  # 当前是递增
10                if not is_increasing:   # 如果之前是递减，现在变为递增
11                    is_increasing = True
12                    count += 1          # 增加一段
13                    q = i - 1           # 记录递减→递增的转折点
14            elif nums[i - 1] > nums[i]:  # 当前是递减
15                if is_increasing:        # 如果之前是递增，现在变为递减
16                    is_increasing = False
17                    count += 1          # 增加一段
18                    p = i - 1           # 记录递增→递减的转折点
19            else:  # 相邻元素相等，不符合严格单调
20                return False
21
22        # 最终检查条件：
23        # 1. 最后一段必须是递增 (is_increasing == True)
24        # 2. 必须有且只有三段 (count == 3)
25        # 3. p必须在有效范围 (0 < p < n-1)
26        # 4. p < q < n-1 满足边界条件
27        return is_increasing and count == 3 and p > 0 and p < q and q < (len(nums) - 1)
28
29# 时间复杂度：O(n)，其中 n 是数组长度
30# - 只进行了一次数组遍历
31# - 每个元素只访问一次
32# - 所有操作都是常数时间
33
34# 空间复杂度：O(1)
35# - 只使用了固定数量的变量（count, is_increasing, p, q）
36# - 不随输入规模增加而增加额外空间