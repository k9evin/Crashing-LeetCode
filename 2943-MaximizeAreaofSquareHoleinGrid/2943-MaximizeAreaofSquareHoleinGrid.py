# Last updated: 1/15/2026, 12:12:02 AM
1class Solution:
2    def maximizeSquareHoleArea(
3        self, n: int, m: int, hBars: List[int], vBars: List[int]
4    ) -> int:
5        # 排序便于找连续的bars
6        hBars.sort()
7        vBars.sort()
8
9        # 记录水平和垂直方向的最大连续bars数量
10        hmax, vmax = 1, 1
11        hcur, vcur = 1, 1
12
13        # 找水平方向最长的连续bars
14        for i in range(1, len(hBars)):
15            if hBars[i] == hBars[i - 1] + 1:
16                hcur += 1  # 连续，计数+1
17            else:
18                hcur = 1  # 不连续，重新计数
19            hmax = max(hmax, hcur)
20
21        # 找垂直方向最长的连续bars
22        for i in range(1, len(vBars)):
23            if vBars[i] == vBars[i - 1] + 1:
24                vcur += 1  # 连续，计数+1
25            else:
26                vcur = 1  # 不连续，重新计数
27            vmax = max(vmax, vcur)
28
29        # 正方形边长 = min(水平连续数, 垂直连续数) + 1
30        side = min(hmax, vmax) + 1
31
32        # 返回面积
33        return side**2
34
35# Time Complexity: O(H log H + V log V) - H和V分别是hBars和vBars的长度（排序主导）
36# Space Complexity: O(1) - 只使用常数个变量（不算排序的空间）