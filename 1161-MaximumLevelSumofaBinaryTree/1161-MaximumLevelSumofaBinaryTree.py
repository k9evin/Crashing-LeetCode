# Last updated: 1/5/2026, 11:19:52 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
9        max_level = 1
10        max_sum = float("-inf")
11        level = 1
12
13        q = deque([root])
14
15        while q:
16            curr_sum = 0
17
18            for _ in range(len(q)):
19                node = q.popleft()
20                curr_sum += node.val
21
22                if node.left:
23                    q.append(node.left)
24                if node.right:
25                    q.append(node.right)
26
27            if curr_sum > max_sum:
28                max_sum = curr_sum
29                max_level = level
30
31            level += 1
32
33        return max_level
34