# Last updated: 1/20/2026, 6:50:48 PM
1class Solution:
2    def minBitwiseArray(self, nums: List[int]) -> List[int]:
3        ans = []
4        for num in nums:
5            found = False
6            # 从 0 开始枚举，找到第一个满足条件的
7            for candidate in range(num):
8                if candidate | (candidate + 1) == num:
9                    ans.append(candidate)
10                    found = True
11                    break
12            if not found:
13                ans.append(-1)
14        return ans
15