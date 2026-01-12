# Last updated: 1/12/2026, 12:15:27 AM
1class Solution:
2    def largestRectangleArea(self, heights):
3        # Add sentinel values (0) at both ends to simplify boundary handling
4        heights = [0] + heights + [0]
5        stack = [0]  # Stack stores indices in increasing height order
6        max_area = 0
7
8        for i in range(1, len(heights)):
9            # Pop bars when current height is lower
10            # Each popped bar serves as the shortest bar in a rectangle
11            while heights[i] < heights[stack[-1]]:
12                stack_i = stack.pop()
13                h = heights[stack_i]
14
15                # Calculate rectangle boundaries
16                l_boundary = stack[-1]  # Left boundary (exclusive)
17                r_boundary = i  # Right boundary (exclusive)
18                w = r_boundary - l_boundary - 1
19
20                max_area = max(max_area, h * w)
21            stack.append(i)
22
23        return max_area
24
25    def maximalRectangle(self, matrix: List[List[str]]) -> int:
26        # Handle edge case: empty matrix
27        if not matrix:
28            return 0
29
30        rows, cols = len(matrix), len(matrix[0])
31        max_area = 0
32        heights = [0] * cols  # Histogram heights for each column
33
34        # Process each row as the base of a histogram
35        for r in range(rows):
36            # Update heights: accumulate consecutive 1's from top to current row
37            for c in range(cols):
38                if matrix[r][c] == "1":
39                    heights[c] += 1  # Extend bar upward
40                else:
41                    heights[c] = 0  # Reset bar (broken by '0')
42
43            # Calculate max rectangle for current histogram
44            # Each row could potentially contain the maximum rectangle
45            max_area = max(max_area, self.largestRectangleArea(heights))
46
47        return max_area
48
49        # Time Complexity: O(m * n)
50        # - m = number of rows, n = number of columns
51        # - For each row: update heights O(n) + largestRectangleArea O(n)
52        # - Total: O(m * n)
53
54        # Space Complexity: O(n)
55        # - heights array: O(n)
56        # - stack in largestRectangleArea: O(n)
57        # - Modified heights in largestRectangleArea: O(n)
58        # - Overall: O(n)
59