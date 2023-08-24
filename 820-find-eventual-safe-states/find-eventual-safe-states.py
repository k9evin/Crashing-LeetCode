class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = set()
        res = []

        def dfs(node):
            if node in visited:
                return False
            if graph[node] == []:
                return True
            visited.add(node)
            for n in graph[node]:
                if not dfs(n):
                    return False
            visited.remove(node)
            graph[node] = []
            return True

        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res
                