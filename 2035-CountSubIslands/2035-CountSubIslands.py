# Last updated: 12/29/2025, 1:40:50 AM
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        res = 0
        m = len(grid2)
        n = len(grid2[0])

        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if grid[i][j] == 0:
                return
            grid[i][j] = 0
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    dfs(grid2, i, j)
        
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    res += 1
                    dfs(grid2, i, j)

        return res

