# Last updated: 1/16/2026, 4:54:02 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        def dfs(node, depth):
10            if not node:
11                return depth
12
13            l_depth = dfs(node.left, depth + 1)
14            r_depth = dfs(node.right, depth + 1)
15
16            return max(l_depth, r_depth)
17
18        return dfs(root, 0)
19