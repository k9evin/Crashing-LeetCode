# Last updated: 1/8/2026, 6:26:18 PM
1class Solution:
2    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
3        n, m = len(nums1), len(nums2)
4
5        # dp[i][j] 表示：考虑 nums1 的前 i 个元素 和 nums2 的前 j 个元素时，
6        # 能获得的最大点积值（注意：必须至少选择一对元素，不能全不选）
7        # 初始化为极小值，因为题目允许负数，且要求非空子序列
8        dp = [[-(10**9)] * (m + 1) for _ in range(n + 1)]
9
10        # 逐个考虑 nums1 和 nums2 中的每个位置
11        for i in range(1, n + 1):
12            for j in range(1, m + 1):
13                # 计算当前两个元素的乘积：nums1[i-1] 和 nums2[j-1]
14                current_pair_product = nums1[i - 1] * nums2[j - 1]
15
16                # 选择一：只使用当前这一对元素（放弃之前的所有选择）
17                # 这在之前的最优解是负数、而当前乘积是正数时特别有用
18                start_fresh = current_pair_product
19
20                # 选择二：将当前这一对元素添加到之前的最佳子序列中
21                # 即：之前用前 i-1 和 j-1 个元素得到的最佳结果 + 当前乘积
22                extend_previous = dp[i - 1][j - 1] + current_pair_product
23
24                # 选择三：跳过 nums2 的当前元素（即不使用 nums2[j-1]）
25                # 那么结果就等于只考虑前 j-1 个元素时的结果
26                skip_nums2_current = dp[i][j - 1]
27
28                # 选择四：跳过 nums1 的当前元素（即不使用 nums1[i-1]）
29                # 那么结果就等于只考虑前 i-1 个元素时的结果
30                skip_nums1_current = dp[i - 1][j]
31
32                # 在所有可能的选择中取最大值作为当前状态的最优解
33                dp[i][j] = max(
34                    start_fresh, extend_previous, skip_nums2_current, skip_nums1_current
35                )
36
37        # 返回考虑所有元素时的最大点积
38        return dp[n][m]
39
40
41# 算法核心思想：
42# 对于每一对位置 (i,j)，我们决定是否要"配对" nums1[i-1] 和 nums2[j-1]
43# 如果配对，可以选择"重新开始"或者"延续之前的配对"
44# 如果不配对，可以选择跳过 nums1 的当前元素或 nums2 的当前元素
45#
46# 时间复杂度: O(n × m) - 需要填充 n×m 的 DP 表
47# 空间复杂度: O(n × m) - 存储完整的 DP 表便于理解逻辑
48