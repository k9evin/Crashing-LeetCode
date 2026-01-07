# Last updated: 1/7/2026, 12:23:42 PM
1class Solution:
2    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
3        # Initialize Union-Find (Disjoint Set Union) structures
4        parent = [
5            i for i in range(len(edges) + 1)
6        ]  # Each node is its own parent initially
7        rank = [1] * (len(edges) + 1)  # Rank (size) of each component
8
9        # Find with path compression: returns root of the set containing 'n'
10        def find(n):
11            if parent[n] != n:
12                parent[n] = find(parent[n])  # Path compression: flatten the structure
13            return parent[n]
14
15        # Union by rank: merges sets containing n1 and n2
16        # Returns False if they are already in the same set (i.e., edge is redundant)
17        def union(n1, n2):
18            p1, p2 = find(n1), find(n2)
19            if p1 == p2:
20                return False  # Already connected → this edge creates a cycle
21
22            # Union by rank: attach smaller tree under root of larger tree
23            if rank[p1] > rank[p2]:
24                parent[p2] = p1
25                rank[p1] += rank[p2]
26            else:
27                parent[p1] = p2
28                rank[p2] += rank[p1]
29
30            return True  # Successfully merged two components
31
32        # Process edges in order (as per problem: return last edge that forms a cycle)
33        for n1, n2 in edges:
34            if not union(n1, n2):
35                return [n1, n2]  # First (and last in input order) redundant edge
36
37
38# Time Complexity: O(n α(n)) ≈ O(n), where n = number of edges
39#   - α(n) is the inverse Ackermann function, effectively constant for all practical inputs
40#   - Each find/union operation is nearly O(1) due to path compression and union by rank
41# Space Complexity: O(n)
42#   - We store parent and rank arrays of size n+1 (nodes are 1-indexed up to n)
43