# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right
            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left
            # 只要 p.val 和 q.val 不是都大于(小于) root.val，就只有三种情况：
            # p 和 q 分居 root 的左、右子树。
            # root 就是 p，q 在 p 的子树中。
            # root 就是 q，p 在 q 的子树中
            else:
                return curr