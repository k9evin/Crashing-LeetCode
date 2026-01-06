# Last updated: 1/6/2026, 1:11:21 AM
1class Solution:
2    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
3        neg_count = 0  # Count of negative numbers in the matrix
4        max_matrix_sum = 0  # Accumulated sum of absolute values of all elements
5        min_abs_val = float("inf")  # Track the smallest absolute value in the matrix
6
7        # Traverse every element in the matrix
8        for row in matrix:
9            for val in row:
10                if val < 0:
11                    neg_count += 1  # Count negatives
12                max_matrix_sum += abs(val)  # Add absolute value to total sum
13                min_abs_val = min(
14                    min_abs_val, abs(val)
15                )  # Update minimum absolute value
16
17        # Key insight: we can flip signs of any two adjacent elements using operations,
18        # which effectively allows us to change the sign of any two elements.
19        # Thus, if the number of negatives is even, we can make all values positive.
20        # If odd, we must leave exactly one negative — best to leave the one with smallest absolute value.
21        if neg_count % 2 != 0:
22            # Subtract twice the smallest absolute value (because we counted it as positive,
23            # but it must remain negative: +x → -x means total reduction of 2x)
24            max_matrix_sum -= 2 * min_abs_val
25
26        return max_matrix_sum
27
28
29# Time Complexity: O(m * n) where m = number of rows, n = number of columns
30#   - We visit each element exactly once
31# Space Complexity: O(1)
32#   - Only using a few extra variables regardless of input size
33