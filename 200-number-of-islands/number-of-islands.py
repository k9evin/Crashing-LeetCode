class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        m = len(grid)
        n = len(grid[0])

        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)


        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(grid, i, j)
        return islands