# Last updated: 1/20/2026, 8:25:46 PM
1class Solution:
2    def minBitwiseArray(self, nums: List[int]) -> List[int]:
3        ans = []
4
5        for num in nums:
6            min_val = -1  # 默认无解
7
8            # 枚举所有可能的值，找到最小的满足条件的 i
9            for i in range(1, num):
10                if (i | (i + 1)) == num:  # 检查 i OR (i+1) 是否等于 num
11                    min_val = i
12                    break  # 找到最小值后立即退出
13
14            ans.append(min_val)
15
16        return ans
17
18
19# Time Complexity: O(n * m)
20#   - n = len(nums)
21#   - m = max value in nums (最坏情况下枚举到 num-1)
22#   - 对于每个 num，最多检查 num-1 次
23
24# Space Complexity: O(1)
25#   - 不计算输出数组，只使用常数额外空间
26#   - 如果计算输出：O(n)
27