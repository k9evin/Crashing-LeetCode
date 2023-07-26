# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.dfs(root, res)
        # return the k-th smallest value (1-indexed)
        return res[k - 1]
        

    def dfs(self, root: Optional[TreeNode], list: List[int]) -> List[int]:
        # in oder traversal to get the ordered array
        if not root:
            return
        self.dfs(root.left, list)
        list.append(root.val)
        self.dfs(root.right, list)