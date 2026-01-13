# Last updated: 1/12/2026, 11:28:26 PM
1class Solution:
2    def hasPath(
3        self, maze: List[List[int]], start: List[int], destination: List[int]
4    ) -> bool:
5        m, n = len(maze), len(maze[0])
6        # Use set to track visited positions where the ball stops
7        visited = set()
8
9        def dfs(x, y):
10            # Pruning: if current position already visited, return False
11            if (x, y) in visited:
12                return False
13            # Base case: reached destination
14            if [x, y] == destination:
15                return True
16
17            # Mark current stop position as visited
18            visited.add((x, y))
19
20            # Four directions: up, down, left, right
21            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
22
23            # Try rolling in all four directions
24            for dx, dy in directions:
25                nx, ny = x, y
26
27                # Simulate ball rolling: keep rolling until hitting a wall or boundary
28                while (
29                    0 <= nx + dx < m
30                    and 0 <= ny + dy < n
31                    and maze[nx + dx][ny + dy] == 0
32                ):
33                    nx += dx
34                    ny += dy
35
36                # Continue DFS from the stop position
37                if dfs(nx, ny):
38                    return True
39
40            # No path found in all four directions
41            return False
42
43        return dfs(start[0], start[1])
44
45
46"""
47Time Complexity: O(m * n * (m + n))
48- m rows, n columns
49- Each cell is visited at most once: O(m * n)
50- For each cell, the while loop rolls at most m steps (vertical) or n steps (horizontal)
51- Total: O(m * n) positions * O(m + n) rolling operations per position
52
53Space Complexity: O(m * n)
54- visited set: O(m * n) to store at most all positions
55- Recursion call stack: O(m * n) in worst case
56"""
57