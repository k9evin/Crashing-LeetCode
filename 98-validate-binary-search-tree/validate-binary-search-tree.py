# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkBST(root, None, None)
    
    def checkBST(self, root: Optional[TreeNode], min, max) -> bool:
        # keep track of the min and max val, because the 
        # root val should always greater than the left side
        # and always less than the right side
        if not root:
            return True
        if min and root.val <= min.val:
            return False
        if max and root.val >= max.val:
            return False
        return (self.checkBST(root.left, min, root) and
                self.checkBST(root.right, root, max))
