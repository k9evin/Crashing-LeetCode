"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Solution 1:
        # Time complexity: O(n)
        # Space complexity: O(n)
        # 特殊情况：如果cur.next是None时，返回None
        old_to_new = {None : None}
        
        # 第一遍：创建新的Node，并添加到字典中
        cur = head
        while cur:
            copy = Node(cur.val)
            old_to_new[cur] = copy
            cur = cur.next
        
        # 第二遍：取回copy，并设置其next和random
        cur = head
        while cur:
            copy = old_to_new[cur]
            copy.next = old_to_new[cur.next]
            copy.random = old_to_new[cur.random]
            cur = cur.next
            
        # 返回head的copy
        return old_to_new[head]
        