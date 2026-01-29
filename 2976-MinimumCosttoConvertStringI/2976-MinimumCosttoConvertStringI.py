# Last updated: 1/29/2026, 5:43:42 PM
1class Solution:
2    def minimumCost(
3        self,
4        source: str,
5        target: str,
6        original: List[str],
7        changed: List[str],
8        cost: List[int],
9    ) -> int:
10        inf = float("inf")
11        dist = [[inf] * 26 for _ in range(26)]
12
13        for i in range(26):
14            dist[i][i] = 0
15
16        for o, c, z in zip(original, changed, cost):
17            u = ord(o) - 97
18            v = ord(c) - 97
19            dist[u][v] = min(dist[u][v], z)
20
21        for k in range(26):
22            for i in range(26):
23                if dist[i][k] == inf:
24                    continue
25                for j in range(26):
26                    if dist[k][j] != inf:
27                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
28
29        total_cost = 0
30        for s_char, t_char in zip(source, target):
31            u = ord(s_char) - 97
32            v = ord(t_char) - 97
33            if u == v:
34                continue
35            if dist[u][v] == inf:
36                return -1
37            total_cost += dist[u][v]
38
39        return total_cost
40