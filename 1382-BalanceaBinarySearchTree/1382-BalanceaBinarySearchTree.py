# Last updated: 2/9/2026, 6:24:31 PM
1class Solution:
2    def balanceBST(self, root: TreeNode) -> TreeNode:
3        # Create a list to store the inorder traversal of the BST
4        inorder = []
5        self.inorder_traversal(root, inorder)
6
7        # Construct and return the balanced BST
8        return self.create_balanced_bst(inorder, 0, len(inorder) - 1)
9
10    def inorder_traversal(self, root: TreeNode, inorder: list):
11        # Perform an inorder traversal to store the elements in sorted order
12        if not root:
13            return
14        self.inorder_traversal(root.left, inorder)
15        inorder.append(root.val)
16        self.inorder_traversal(root.right, inorder)
17
18    def create_balanced_bst(
19        self, inorder: list, start: int, end: int
20    ) -> TreeNode:
21        # Base case: if the start index is greater than the end index, return None
22        if start > end:
23            return None
24
25        # Find the middle element of the current range
26        mid = start + (end - start) // 2
27
28        # Recursively construct the left and right subtrees
29        left_subtree = self.create_balanced_bst(inorder, start, mid - 1)
30        right_subtree = self.create_balanced_bst(inorder, mid + 1, end)
31
32        # Create a new node with the middle element and attach the subtrees
33        node = TreeNode(inorder[mid], left_subtree, right_subtree)
34        return node
35