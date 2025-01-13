class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Algorithm:
        - Iterate through the grid to find all land cells ('1').
        - Use Depth-First Search (DFS) to traverse and mark all connected land cells as visited ('0').
        - Increment the island count for each DFS initiation.

        Time Complexity: O(m * n), where m is the number of rows and n is the number of columns.
                         Each cell is visited once during the traversal.
        Space Complexity: O(m * n) in the worst case for the DFS recursion stack, if the grid is completely filled with land.
        """

        if not grid:  # Edge case: empty grid
            return 0

        island_count = 0  # Initialize count of islands
        rows, cols = len(grid), len(grid[0])  # Dimensions of the grid

        def dfs(i: int, j: int) -> None:
            """
            Depth-First Search to mark all connected land cells ('1') as visited ('0').
            """
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == "0":
                return  # Stop recursion for out-of-bounds or water cells
            grid[i][j] = "0"  # Mark the current cell as visited

            # Recursively visit all 4 adjacent cells
            dfs(i + 1, j)  # Down
            dfs(i - 1, j)  # Up
            dfs(i, j + 1)  # Right
            dfs(i, j - 1)  # Left

        # Traverse the grid
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":  # Found a new island
                    island_count += 1  # Increment island count
                    dfs(i, j)  # Perform DFS to mark all connected land cells as visited

        return island_count  # Return total number of islands
