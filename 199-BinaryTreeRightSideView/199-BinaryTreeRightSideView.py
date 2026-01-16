# Last updated: 1/16/2026, 8:52:45 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
9        if root is None:
10            return []
11
12        queue = deque([root])
13        rightside = []
14
15        while queue:
16            rightside.append(queue[-1].val)
17
18            for i in range(len(queue)):
19                node = queue.popleft()
20                if node.left:
21                    queue.append(node.left)
22                if node.right:
23                    queue.append(node.right)
24
25        return rightside
26