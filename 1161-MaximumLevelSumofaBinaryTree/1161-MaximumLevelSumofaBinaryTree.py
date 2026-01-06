# Last updated: 1/5/2026, 11:20:54 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
9        max_level = 1  # Level with maximum sum (1-indexed)
10        max_sum = float("-inf")  # Maximum sum found so far
11        level = 1  # Current level being processed
12
13        # BFS queue initialized with root node
14        q = deque([root])
15
16        # Process tree level by level using BFS
17        while q:
18            curr_sum = 0  # Sum of node values at current level
19
20            # Process all nodes at the current level (fixed queue size)
21            for _ in range(len(q)):
22                node = q.popleft()
23                curr_sum += node.val
24
25                # Add children to queue for next level processing
26                if node.left:
27                    q.append(node.left)
28                if node.right:
29                    q.append(node.right)
30
31            # Update maximum sum and corresponding level if current sum is greater
32            if curr_sum > max_sum:
33                max_sum = curr_sum
34                max_level = level
35
36            level += 1  # Move to next level
37
38        return max_level
39
40
41# Time Complexity: O(N) where N is the number of nodes in the tree
42#   - Each node is visited exactly once during BFS traversal
43# Space Complexity: O(W) where W is the maximum width of the tree
44#   - In worst case (complete binary tree), the last level contains ~N/2 nodes
45#   - Thus space complexity is O(N) for the BFS queue
46