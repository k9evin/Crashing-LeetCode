# Last updated: 1/9/2026, 9:35:25 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        def dfs(node):
10            # 空子树：没有节点，高度为 0；也没有候选根
11            if not node:
12                return None, 0
13
14            # 分别递归得到左右子树：
15            # - l_node / r_node：左右子树各自的“最小包含最深节点子树”的根
16            # - l_height / r_height：左右子树高度
17            l_node, l_height = dfs(node.left)
18            r_node, r_height = dfs(node.right)
19
20            # 左边更深：最深节点全部出现在左子树，答案继承左子树的候选根
21            if l_height > r_height:
22                return l_node, l_height + 1
23
24            # 右边更深：同理
25            elif l_height < r_height:
26                return r_node, r_height + 1
27
28            # 一样深：最深节点分布在左右两边（至少两边都能达到该深度）
29            # 要同时包含它们，最小子树根就是当前 node（相当于 LCA）
30            else:
31                # 这里写 l_height + 1 或 r_height + 1 都一样，因为两者相等
32                return node, l_height + 1
33
34        res, _ = dfs(root)
35        return res
36
37        # Time Complexity: O(n)  — 每个节点只访问一次
38        # Space Complexity: O(h) — 递归栈深度，h 为树高；最坏退化链表时 O(n)
39