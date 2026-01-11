# Last updated: 1/11/2026, 6:25:35 PM
1class Solution:
2
3    def maximalRectangle(self, matrix: List[List[str]]) -> int:
4        if not matrix:
5            return 0
6
7        m = len(matrix)
8        n = len(matrix[0])
9
10        left = [0] * n  # initialize left as the leftmost boundary possible
11        right = [n] * n  # initialize right as the rightmost boundary possible
12        height = [0] * n
13
14        maxarea = 0
15
16        for i in range(m):
17
18            cur_left, cur_right = 0, n
19            # update height
20            for j in range(n):
21                if matrix[i][j] == "1":
22                    height[j] += 1
23                else:
24                    height[j] = 0
25            # update left
26            for j in range(n):
27                if matrix[i][j] == "1":
28                    left[j] = max(left[j], cur_left)
29                else:
30                    left[j] = 0
31                    cur_left = j + 1
32            # update right
33            for j in range(n - 1, -1, -1):
34                if matrix[i][j] == "1":
35                    right[j] = min(right[j], cur_right)
36                else:
37                    right[j] = n
38                    cur_right = j
39            # update the area
40            for j in range(n):
41                maxarea = max(maxarea, height[j] * (right[j] - left[j]))
42
43        return maxarea