// Last updated: 1/12/2026, 11:13:54 PM
1/**
2 * Time Complexity: O(m * n * (m + n))
3 * - m rows, n columns
4 * - Each cell is visited at most once: O(m * n)
5 * - For each cell, the while loop rolls at most m steps (vertical) or n steps (horizontal)
6 * - Total: O(m * n) positions * O(m + n) rolling operations per position
7 * 
8 * Space Complexity: O(m * n)
9 * - visited array: O(m * n)
10 * - Recursion call stack: O(m * n) in worst case
11 */
12class Solution {
13    public boolean hasPath(int[][] maze, int[] start, int[] destination) {
14        // Track visited positions where the ball stops
15        boolean[][] visited = new boolean[maze.length][maze[0].length];
16
17        return dfs(maze, start, destination, visited);
18    }
19
20    private boolean dfs(int[][] maze, int[] curr, int[] destination, boolean[][] visited) {
21        // Pruning: if current position already visited, return false to avoid duplicate search
22        if (visited[curr[0]][curr[1]]) {
23            return false;
24        }
25
26        // Base case: reached destination
27        if (curr[0] == destination[0] && curr[1] == destination[1]) {
28            return true;
29        }
30
31        // Mark current stop position as visited
32        visited[curr[0]][curr[1]] = true;
33
34        // Four directions: up, down, left, right
35        int[][] directions = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
36
37        // Try rolling in all four directions
38        for (int[] dir : directions) {
39            int r = curr[0], c = curr[1];
40
41            // Simulate ball rolling: keep rolling until hitting a wall or boundary
42            while (r >= 0 && r < maze.length && c >= 0 && c < maze[0].length && maze[r][c] == 0) {
43                r += dir[0];
44                c += dir[1];
45            }
46
47            // Step back one position to get where the ball actually stops (r,c is now wall/out of bounds)
48            r -= dir[0];
49            c -= dir[1];
50
51            // Continue DFS from the stop position, return true if path found
52            if (dfs(maze, new int[] { r, c }, destination, visited)) {
53                return true;
54            }
55        }
56        
57        // No path found in all four directions
58        return false;
59    }
60}