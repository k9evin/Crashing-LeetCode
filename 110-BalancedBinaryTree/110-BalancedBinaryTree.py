# Last updated: 2/8/2026, 5:44:15 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        def dfs(node: Optional[TreeNode]) -> int:
10            if not node:
11                return 0
12
13            # Early exit: stop if left subtree is already unbalanced
14            left_depth = dfs(node.left)
15            if left_depth == -1:
16                return -1
17
18            # Only process right subtree if left is balanced
19            right_depth = dfs(node.right)
20            if right_depth == -1 or abs(left_depth - right_depth) > 1:
21                return -1
22
23            return max(left_depth, right_depth) + 1
24
25        return dfs(root) != -1
26
27
28# Time Complexity: O(n)  # 每个节点仅访问一次，最坏情况遍历所有节点
29# Space Complexity: O(h) # 递归栈深度等于树高h，平均logn，最坏n（链式结构）
30