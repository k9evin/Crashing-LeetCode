class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        # Solution 1:
        # Time complexity: O(q * (m + n) + m * n) 
        # q is the length of the indices
        # Space complexity: O(m * n)
        # matrix = [[0] * n for _ in range(m)]
        # for i, j in indices:
        #     # update the row
        #     for c in range(n):
        #         matrix[i][c] += 1
        #     # update the column
        #     for r in range(m):
        #         matrix[r][j] += 1
        # return sum(x % 2 for row in matrix for x in row)
		
		# Solution 2:
        # Time complexity: O(q + m * n)
        # Space complexity: O(m + n)
        rows, cols = [0] * m, [0] * n
        for i, j in indices:
            rows[i] += 1
            cols[j] += 1
        return sum((r + c) % 2 for r in rows for c in cols)