class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # set不允许重复
        po = set()
        ao = set()

        m = len(heights)
        n = len(heights[0])

        # 换一种思路，水往高处流。看从海出发能到达哪些点
        def dfs(i, j, visited, prev_height):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if heights[i][j] < prev_height:
                return
            if (i, j) in visited:
                return 
            visited.add((i, j))
            dfs(i, j + 1, visited, heights[i][j])
            dfs(i, j - 1, visited, heights[i][j])
            dfs(i + 1, j, visited, heights[i][j])
            dfs(i - 1, j, visited, heights[i][j])

        # 左右
        for i in range(m):
            dfs(i, 0, po, heights[i][0])
            dfs(i, n - 1, ao, heights[i][n - 1])

        # 上下
        for j in range(n):
            dfs(0, j, po, heights[0][j])
            dfs(m - 1, j, ao, heights[m - 1][j])

        return list(po & ao)