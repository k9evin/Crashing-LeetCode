# Last updated: 1/7/2026, 5:09:09 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxProduct(self, root: Optional[TreeNode]) -> int:
9        MOD = 10**9 + 7
10        all_sums = []  # Store sum of every subtree in the tree
11
12        # Helper function to compute subtree sums via post-order traversal
13        def tree_sum(node):
14            if node is None:
15                return 0
16
17            left_sum = tree_sum(node.left)  # Sum of left subtree
18            right_sum = tree_sum(node.right)  # Sum of right subtree
19
20            total_sum = node.val + left_sum + right_sum  # Sum of current subtree
21            all_sums.append(total_sum)  # Record this subtree's sum
22
23            return total_sum
24
25        total = tree_sum(root)  # Total sum of the entire tree
26        max_split_sum = 0  # Track maximum product of split
27
28        # For each possible subtree (represented by its sum 's'),
29        # the other part after removing its edge has sum = total - s
30        # Product = s * (total - s)
31        for s in all_sums:
32            max_split_sum = max(max_split_sum, s * (total - s))
33
34        return max_split_sum % MOD
35
36
37# Time Complexity: O(N), where N is the number of nodes in the tree
38#   - We traverse the tree once to compute all subtree sums (O(N))
39#   - Then iterate through all_sums (which has N elements) to find max product (O(N))
40# Space Complexity: O(N)
41#   - Storing all subtree sums in all_sums list (O(N))
42#   - Recursion stack depth up to O(N) in worst case (skewed tree)
43