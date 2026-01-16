# Last updated: 1/16/2026, 7:04:29 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
9        # Both trees are empty
10        if p is None and q is None:
11            return True
12
13        # One tree is empty, the other is not
14        if p is None or q is None:
15            return False
16
17        # Values don't match
18        if p.val != q.val:
19            return False
20
21        # Recursively check left and right subtrees
22        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
23
24
25# Time Complexity: O(n) - each node is visited once
26# Space Complexity: O(h) - recursion stack depth equals tree height
27#   - Best case (balanced tree): O(log n)
28#   - Worst case (skewed tree): O(n)
29