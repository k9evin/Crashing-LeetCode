# Last updated: 1/16/2026, 5:03:12 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        def dfs(node, depth):
10            # Base case: reached a null node (empty tree or leaf's child)
11            # Return the current depth (distance from root to this null node)
12            if not node:
13                return depth
14
15            # Recursively explore left subtree, incrementing depth by 1
16            l_depth = dfs(node.left, depth + 1)
17
18            # Recursively explore right subtree, incrementing depth by 1
19            r_depth = dfs(node.right, depth + 1)
20
21            # Return the maximum depth found in either subtree
22            # This propagates the deepest path up the recursion stack
23            return max(l_depth, r_depth)
24
25        # Start DFS traversal from root with initial depth 0
26        # For empty tree (root is None), dfs immediately returns 0
27        return dfs(root, 0)
28
29
30# Time Complexity: O(n) - Each node is visited exactly once
31# Space Complexity: O(h) where h is the height of the tree
32#   - Best case (balanced tree): O(log n)
33#   - Worst case (skewed tree): O(n) - recursion stack depth equals number of nodes
34#   - Average case: O(log n) for randomly constructed trees
35