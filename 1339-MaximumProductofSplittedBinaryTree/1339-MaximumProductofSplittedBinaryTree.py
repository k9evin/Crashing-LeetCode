# Last updated: 1/7/2026, 5:01:40 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxProduct(self, root: Optional[TreeNode]) -> int:
9        MOD = 10**9 + 7
10        all_sums = []
11
12        def tree_sum(node):
13            if node is None:
14                return 0
15
16            left_sum = tree_sum(node.left)
17            right_sum = tree_sum(node.right)
18
19            total_sum = node.val + left_sum + right_sum
20            all_sums.append(total_sum)
21
22            return total_sum
23
24        total = tree_sum(root)
25        max_split_sum = 0
26
27        for s in all_sums:
28            max_split_sum = max(max_split_sum, s * (total - s))
29
30        return max_split_sum % MOD
31