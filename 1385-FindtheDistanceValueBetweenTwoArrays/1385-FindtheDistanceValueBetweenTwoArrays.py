# Last updated: 1/16/2026, 8:58:40 PM
1class Solution:
2    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
3        # 步骤1：对arr2排序，为二分查找做准备
4        arr2.sort()
5        count = 0
6
7        # 步骤2：遍历arr1中的每个元素x，判断是否符合条件
8        for x in arr1:
9            # 计算x的"危险区间"：若arr2中存在元素落在这个区间内，则x不符合条件
10            forbidden_start = x - d
11            forbidden_end = x + d
12
13            # 左右开区间二分查找：寻找arr2中第一个≥forbidden_start的元素位置
14            # 初始区间：(-1, len(arr2))，表示从比第一个索引还小的位置开始，到比最后一个索引大的位置结束
15            left, right = -1, len(arr2)
16
17            while left + 1 < right:  # 当区间内至少有一个元素时继续循环
18                mid = left + (right - left) // 2
19                if arr2[mid] >= forbidden_start:
20                    # 找到一个可能的候选位置，尝试向左缩小范围（因为要找第一个≥forbidden_start的元素）
21                    right = mid
22                else:
23                    # arr2[mid]太小，需要向右扩大范围
24                    left = mid
25
26            # 循环结束后，right指向arr2中第一个≥forbidden_start的元素
27            # 此时有两种情况：
28            # 1. right == len(arr2) → arr2中所有元素都小于forbidden_start → 无元素落在危险区间内
29            # 2. arr2[right] > forbidden_end → 第一个≥forbidden_start的元素已超出危险区间上限 → 无元素落在危险区间内
30            if right >= len(arr2) or arr2[right] > forbidden_end:
31                count += 1
32
33        return count
34
35
36# 时间复杂度：O(n log n + m log n)
37#   - 排序arr2：O(n log n)，其中n是arr2的长度
38#   - 每个arr1元素的二分查找：O(log n)，共m次，总O(m log n)
39# 空间复杂度：O(1)（原地排序，仅使用常数额外空间）
40