# Last updated: 1/16/2026, 7:27:58 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
9        # Compare left and right subtrees for mirror symmetry
10        return self.isMirror(root.left, root.right)
11
12    def isMirror(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
13        # Both nodes are None - symmetric
14        if p is None and q is None:
15            return True
16
17        # One is None, other isn't - not symmetric
18        if p is None or q is None:
19            return False
20
21        # Values don't match - not symmetric
22        if p.val != q.val:
23            return False
24
25        # Recursively check mirror symmetry:
26        # p.left mirrors q.right and p.right mirrors q.left
27        return self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)
28
29
30# Time Complexity: O(n) - each node visited once
31# Space Complexity: O(h) - recursion stack depth = tree height
32#   - Best case (balanced): O(log n)
33#   - Worst case (skewed): O(n)
34