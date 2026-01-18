# Last updated: 1/18/2026, 6:37:56 PM
1class Solution:
2    def largestMagicSquare(self, grid: List[List[int]]) -> int:
3        m, n = len(grid), len(grid[0])
4
5        # ===== 1. 预处理前缀和 =====
6        # row[i][j]: 第i行前j个元素的和（索引0到j-1）
7        # 为什么是 [m][n+1]？
8        #   - m行：每行需要一个前缀和数组
9        #   - n+1列：多一列用于边界（row[i][0] = 0，表示"前0个元素"）
10        row = [[0] * (n + 1) for _ in range(m)]
11
12        # col[i][j]: 第j列前i个元素的和（索引0到i-1）
13        # 为什么是 [m+1][n]？
14        #   - n列：每列需要一个前缀和数组
15        #   - m+1行：多一行用于边界（col[0][j] = 0，表示"前0个元素"）
16        col = [[0] * n for _ in range(m + 1)]
17
18        # 计算前缀和：O(m*n)
19        for i in range(m):
20            for j in range(n):
21                # 行前缀和：在同一行，从左往右累加
22                row[i][j + 1] = row[i][j] + grid[i][j]
23
24                # 列前缀和：在同一列，从上往下累加
25                col[i + 1][j] = col[i][j] + grid[i][j]
26
27        # ===== 2. 检查函数 =====
28        def is_magic(r, c, k):
29            """
30            检查以 (r, c) 为左上角、边长为 k 的正方形是否为魔方
31
32            参数：
33                r: 正方形左上角的行索引
34                c: 正方形左上角的列索引
35                k: 正方形的边长
36
37            返回：
38                True 如果是魔方，False 否则
39
40            时间复杂度：O(k)
41            """
42            # 计算主对角线和作为目标值
43            # 主对角线：(r,c) → (r+1,c+1) → ... → (r+k-1,c+k-1)
44            # 索引规律：grid[r+i][c+i]，其中 i ∈ [0, k)
45            target = sum(grid[r + i][c + i] for i in range(k))
46
47            # 检查反对角线是否等于目标值
48            # 反对角线：(r,c+k-1) → (r+1,c+k-2) → ... → (r+k-1,c)
49            # 索引规律：grid[r+i][c+k-1-i]，其中 i ∈ [0, k)
50            #   - 行递增：r+i（从上往下）
51            #   - 列递减：c+k-1-i（从右往左）
52            if sum(grid[r + i][c + k - 1 - i] for i in range(k)) != target:
53                return False
54
55            # 检查所有行的和
56            # 第i行的区间 [c, c+k) 的和
57            # 使用前缀和差值：row[i][c+k] - row[i][c]
58            #   - row[i][c+k]：第i行前(c+k)个元素的和（包含索引c到c+k-1）
59            #   - row[i][c]：第i行前c个元素的和（包含索引0到c-1）
60            #   - 差值：索引c到c+k-1的和（正好k个元素）
61            for i in range(r, r + k):
62                if row[i][c + k] - row[i][c] != target:
63                    return False
64
65            # 检查所有列的和
66            # 第j列的区间 [r, r+k) 的和
67            # 使用前缀和差值：col[r+k][j] - col[r][j]
68            #   - col[r+k][j]：第j列前(r+k)个元素的和（包含索引r到r+k-1）
69            #   - col[r][j]：第j列前r个元素的和（包含索引0到r-1）
70            #   - 差值：索引r到r+k-1的和（正好k行）
71            for j in range(c, c + k):
72                if col[r + k][j] - col[r][j] != target:
73                    return False
74
75            return True
76
77        # ===== 3. 主逻辑：从大到小枚举 =====
78        # 贪心策略：从最大可能的边长开始，找到第一个魔方就是答案
79        # 边长范围：[1, min(m, n)]
80        for k in range(min(m, n), 0, -1):
81            # 枚举所有可能的左上角位置
82            # r的范围：[0, m-k]，保证 r+k-1 < m
83            # c的范围：[0, n-k]，保证 c+k-1 < n
84            for r in range(m - k + 1):
85                for c in range(n - k + 1):
86                    if is_magic(r, c, k):
87                        return k  # 找到即返回
88
89        # 兜底：至少1×1是魔方（题目保证）
90        return 1
91
92
93# ========================================
94#           复杂度分析
95# ========================================
96
97"""
98时间复杂度：O(m * n * min(m,n)²)
99  1. 预处理前缀和：O(m*n)
100  2. 枚举边长k：O(min(m,n))
101  3. 枚举左上角：O((m-k)*(n-k)) ≈ O(m*n)
102  4. 每次检查：O(k)（2条对角线 + k行 + k列）
103
104  总计：O(min(m,n) * m*n * k) = O(m*n*min(m,n)²)
105
106  最坏情况：m=n=50 时，约 50*50*50² = 6,250,000 次操作
107
108空间复杂度：O(m * n)
109  - row数组：m * (n+1) = O(m*n)
110  - col数组：(m+1) * n = O(m*n)
111  - 递归深度：O(1)（没有递归）
112
113  总计：O(m*n)
114"""
115