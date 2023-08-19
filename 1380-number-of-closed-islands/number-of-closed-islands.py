class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        res = 0

        m = len(grid)
        n = len(grid[0])

        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if grid[i][j] == 1:
                return
            grid[i][j] = 1
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)
            dfs(grid, i - 1, j)
            dfs(grid, i + 1, j)

        for r in range(m):
            dfs(grid, r, 0)
            dfs(grid, r, n - 1)

        for c in range(n):
            dfs(grid, 0, c)
            dfs(grid, m - 1, c)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    res += 1
                    dfs(grid, i, j)
        return res