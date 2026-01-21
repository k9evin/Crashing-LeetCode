# Last updated: 1/21/2026, 6:42:37 PM
1class Solution:
2    def minBitwiseArray(self, nums: List[int]) -> List[int]:
3        ans = []
4
5        for num in nums:
6            # 偶数无解：因为 ans | (ans+1) 的最低位必为1，不可能得到偶数
7            if num % 2 == 0:
8                ans.append(-1)
9            else:
10                # 统计从最低位开始连续1的个数
11                cnt_ones = 0
12                temp = num
13
14                # temp & 1 检查最低位是否为1
15                # temp >>= 1 右移一位，检查下一位
16                while temp & 1:
17                    cnt_ones += 1
18                    temp >>= 1
19
20                # 答案 = num - 2^(cnt_ones-1)
21                # 把连续1中的最高位（第cnt_ones位）变成0
22                # 1 << (cnt_ones - 1) 等于 2^(cnt_ones-1)
23                ans.append(num - (1 << (cnt_ones - 1)))
24
25        return ans
26
27
28# Time Complexity: O(n * log m)
29#   - n = len(nums)，遍历数组
30#   - log m = 统计连续1的个数，最多 log₂(num) 位
31#   - m = max(nums)，最大值10⁹约有30位二进制
32#   - 对每个数最多循环30次
33
34# Space Complexity: O(1)
35#   - 只使用常数额外空间（cnt_ones, temp）
36#   - 输出数组 ans 不计入额外空间
37