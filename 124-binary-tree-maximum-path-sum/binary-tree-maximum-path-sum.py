# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int: 
        self.maxSum = float('-inf')
        self.depth(root)
        return self.maxSum

    def depth(self, root):
        if not root:
            return 0
        left_val = self.depth(root.left)
        right_val = self.depth(root.right)
        self.maxSum = max(self.maxSum, left_val + right_val + root.val)
        return max(max(left_val, right_val) + root.val, 0)
        