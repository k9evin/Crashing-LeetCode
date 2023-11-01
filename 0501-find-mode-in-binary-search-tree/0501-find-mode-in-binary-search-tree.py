# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        tree_map = collections.defaultdict(int)

        def traverse(root):
            if not root:
                return
            traverse(root.left)
            tree_map[root.val] += 1
            traverse(root.right)

        traverse(root)
        max_freq = max(tree_map.values())
        return [k for k, v in tree_map.items() if v == max_freq]
        