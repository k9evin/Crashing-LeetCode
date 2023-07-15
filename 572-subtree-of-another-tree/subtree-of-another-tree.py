# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 如果root本身就是空的，不会存在subtree
        if not root:
            return False
        if not subRoot:
            return True
        if self.isSameTree(root, subRoot):
            return True
        # 检查子节点是否存在相同的树
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 如果两个nodes都是空的
        if not p and not q:
            return True
        # 如果两个nodes都存在且值都相等
        if (p and q) and (p.val == q.val):
            return (self.isSameTree(p.left, q.left) and 
                    self.isSameTree(p.right, q.right))
        # 其他的情况
        return False
