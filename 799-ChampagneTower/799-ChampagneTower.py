# Last updated: 2/14/2026, 6:49:07 PM
1class Solution:
2    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
3        # current_row: 存储当前已计算行的每个杯子的香槟量
4        # 初始为第 0 行（塔顶），只有 1 个杯子，倒入 poured 杯香槟
5        current_row = [poured]
6
7        # 逐层模拟：从第 1 行计算到第 query_row 行
8        # row_num: 当前正在计算的目标行号
9        for row_num in range(1, query_row + 1):
10            # next_row: 第 row_num 行，有 row_num + 1 个杯子
11            # 初始全部为空（0 杯香槟）
12            next_row = [0] * (row_num + 1)
13
14            # 遍历上一行（current_row）的每个杯子
15            # i: 上一行中第 i 个杯子的索引（0 到 row_num-1）
16            for i in range(row_num):
17                # 计算该杯子的溢出量：
18                # - 如果杯子中 <= 1 杯，则不溢出（max 确保不会为负）
19                # - 如果杯子中 > 1 杯，则多余的部分会溢出
20                overflow = max(current_row[i] - 1, 0)
21
22                # 溢出的香槟平均分给左右两个下方的杯子
23                spill = overflow / 2
24
25                # 左边下方的杯子接收一半溢出
26                next_row[i] += spill
27                # 右边下方的杯子接收一半溢出
28                next_row[i + 1] += spill
29
30            # 完成当前行的计算后，将其设为"上一行"
31            # 继续计算下一层
32            current_row = next_row
33
34        # 返回目标杯子的香槟量，但最多为 1（杯子满了就是 1）
35        return min(1, current_row[query_glass])
36
37
38"""
39时间复杂度（Time Complexity）: O(query_row²)
40- 外层循环执行 query_row 次（从第 1 行到第 query_row 行）
41- 第 row_num 行的内层循环执行 row_num 次
42- 总操作数：1 + 2 + 3 + ... + query_row = query_row * (query_row + 1) / 2
43- 因此时间复杂度为 O(query_row²)，其中 query_row < 100
44
45空间复杂度（Space Complexity）: O(query_row)
46- 我们只保存了两行的数据：current_row 和 next_row
47- 每行最多有 query_row + 1 个元素
48- 因此空间复杂度为 O(query_row)
49"""
50