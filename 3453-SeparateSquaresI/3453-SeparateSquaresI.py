# Last updated: 1/13/2026, 12:11:25 AM
1class Solution:
2    def separateSquares(self, squares: List[List[int]]) -> float:
3        # 初始化最大y坐标和总面积
4        max_y = 0
5        total_area = 0
6
7        # 遍历所有正方形，计算最大y坐标（上界）和总面积
8        for x, y, l in squares:
9            max_y = max(max_y, y + l)  # 正方形顶部的y坐标
10            total_area += l**2  # 累加每个正方形的面积
11
12        # 计算给定y坐标线下方的总面积
13        def curr_area(y_limit):
14            area = 0
15            for x, y, l in squares:
16                # 如果正方形底部在线下方
17                if y < y_limit:
18                    # 计算该正方形在线下方的面积
19                    # 高度为 min(l, y_limit - y)，宽度为 l
20                    area += l * min(l, y_limit - y)
21            return area
22
23        # 二分查找：在 [0, max_y] 范围内找到合适的y坐标
24        lo, hi = 0, max_y
25        eps = 1e-5  # 精度要求
26
27        # 当搜索区间大于精度时继续查找
28        while abs(hi - lo) > eps:
29            mid = lo + (hi - lo) / 2  # 浮点数二分
30            # 如果下方面积 >= 总面积的一半，说明分界线太高，向下找
31            if curr_area(mid) >= total_area / 2:
32                hi = mid
33            # 否则分界线太低，向上找
34            else:
35                lo = mid
36
37        return hi
38
39
40# 时间复杂度：O(n * log(max_y / ε))
41# - n 是正方形的数量
42# - 二分查找迭代次数为 O(log(max_y / ε))，其中 ε = 1e-5 是精度
43# - 每次迭代需要 O(n) 时间计算 curr_area
44#
45# 空间复杂度：O(1)
46# - 只使用了常数个额外变量，不计算输入数组
47