# Last updated: 1/8/2026, 11:20:01 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        def dfs(node, depth):
10            if not node:
11                return None, depth + 1
12
13            left_node, left_depth = dfs(node.left, depth + 1)
14            right_node, right_depth = dfs(node.right, depth + 1)
15
16            if left_depth > right_depth:
17                return left_node, left_depth
18            elif left_depth < right_depth:
19                return right_node, right_depth
20            else:
21                return node, left_depth
22
23        node, _ = dfs(root, 0)
24
25        return node
26