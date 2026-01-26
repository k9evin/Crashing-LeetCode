# Last updated: 1/25/2026, 8:05:57 PM
1class Solution:
2    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
3        arr.sort()
4        res = []
5        min_diff = float("inf")
6
7        for i in range(1, len(arr)):
8            diff = arr[i] - arr[i - 1]
9            if diff < min_diff:
10                min_diff = diff
11                res = [[arr[i - 1], arr[i]]]
12            elif diff == min_diff:
13                res.append([arr[i - 1], arr[i]])
14
15        return res
16