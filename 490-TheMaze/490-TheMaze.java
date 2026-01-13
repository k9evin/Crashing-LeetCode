// Last updated: 1/12/2026, 11:09:54 PM
1class Solution {
2    public boolean hasPath(int[][] maze, int[] start, int[] destination) {
3        boolean[][] visited = new boolean[maze.length][maze[0].length];
4
5        return dfs(maze, start, destination, visited);
6    }
7
8    private boolean dfs(int[][] maze, int[] curr, int[] destination, boolean[][] visited) {
9        if (visited[curr[0]][curr[1]]) {
10            return false;
11        }
12
13        if (curr[0] == destination[0] && curr[1] == destination[1]) {
14            return true;
15        }
16
17        visited[curr[0]][curr[1]] = true;
18
19        int[][] directions = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
20
21        for (int[] dir : directions) {
22            int r = curr[0], c = curr[1];
23
24            while (r >= 0 && r < maze.length && c >= 0 && c < maze[0].length && maze[r][c] == 0) {
25                r += dir[0];
26                c += dir[1];
27            }
28
29            r -= dir[0];
30            c -= dir[1];
31
32            if (dfs(maze, new int[] { r, c }, destination, visited)) {
33                return true;
34            }
35        }
36        return false;
37    }
38}