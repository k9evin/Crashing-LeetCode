# Last updated: 1/16/2026, 8:54:43 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
9        # Handle empty tree edge case
10        if root is None:
11            return []
12
13        # Initialize queue with root node for level-order traversal
14        queue = deque([root])
15        rightside = []
16
17        # Traverse each level of the tree
18        while queue:
19            # Append rightmost node value of current level to result
20            rightside.append(queue[-1].val)
21
22            # Process all nodes in current level, enqueue their children
23            for i in range(len(queue)):
24                node = queue.popleft()
25                # Enqueue left child first to maintain left-to-right order
26                if node.left:
27                    queue.append(node.left)
28                if node.right:
29                    queue.append(node.right)
30
31        return rightside
32
33
34# Time Complexity: O(n) where n is total nodes (each node is visited once)
35# Space Complexity: O(n) (worst case, queue stores all nodes of the widest level, which is up to n/2 for a perfect binary tree)
36