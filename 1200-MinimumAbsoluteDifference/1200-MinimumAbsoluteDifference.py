# Last updated: 1/25/2026, 8:09:52 PM
1class Solution:
2    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
3        # 1. 先排序数组，这样相邻元素的差就是可能的最小绝对差
4        arr.sort()
5
6        res = []  # 存储结果列表
7        min_diff = float("inf")  # 初始化最小差值为无穷大
8
9        # 2. 遍历排序后的数组，计算相邻元素的差值
10        for i in range(1, len(arr)):
11            diff = arr[i] - arr[i - 1]  # 计算当前相邻对的差值
12
13            # 如果发现更小的差值，更新最小差值并重置结果列表
14            if diff < min_diff:
15                min_diff = diff
16                res = [[arr[i - 1], arr[i]]]
17
18            # 如果差值等于当前最小差值，添加到结果列表
19            elif diff == min_diff:
20                res.append([arr[i - 1], arr[i]])
21
22        # 3. 返回所有具有最小绝对差的元素对
23        return res
24
25
26# 时间复杂度：O(n log n)
27# - 排序操作：O(n log n) 占主导
28# - 单次遍历：O(n)
29
30# 空间复杂度：O(k) 其中k是最小差值对的数量
31# - 存储结果列表所需空间
32