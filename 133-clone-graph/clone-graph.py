"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}

        def dfs(node):
            if not node:
                return None
            if node in visited:
                return visited[node]
            # 克隆节点，注意不要克隆它的邻居的列表
            clone = Node(node.val)
            visited[node] = clone
            
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            return clone
        
        return dfs(node)