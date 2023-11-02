# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        # post-order traversal
        def traverse(root):
            nonlocal res

            # base case
            if not root:
                return 0, 0

            # recursively calculate the left and right subtrees' sum and count
            left_sum, left_count = traverse(root.left)
            right_sum, right_count = traverse(root.right)

            # calculate the current sum and count 
            curr_sum = root.val + left_sum + right_sum
            curr_count = 1 + left_count + right_count

            # check if the current node equals to the average of subtree
            if curr_sum // curr_count == root.val:
                res += 1

            # return the curr_sum and curr_count pair
            return curr_sum, curr_count


        res = 0
        traverse(root)
        return res