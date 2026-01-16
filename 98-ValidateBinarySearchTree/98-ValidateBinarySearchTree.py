# Last updated: 1/16/2026, 4:12:29 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: Optional[TreeNode], min=-inf, max=inf) -> bool:
9        # Base case: empty tree is valid BST
10        if not root:
11            return True
12
13        # If current node's value violates BST range constraint, return False immediately
14        # For root node, min=-inf and max=inf initially (no bounds)
15        # For left children, max is updated to parent's value
16        # For right children, min is updated to parent's value
17        if not (min < root.val < max):
18            return False
19
20        # Recursively validate left and right subtrees
21        return self.isValidBST(root.left, min, root.val) and self.isValidBST(
22            root.right, root.val, max
23        )
24
25
26# Time Complexity: O(n) - Each node is visited exactly once
27# Space Complexity: O(h) - Recursion stack height equals tree height (log n for balanced tree, n for skewed tree)
28