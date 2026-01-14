# Last updated: 1/14/2026, 1:32:52 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        # prev: 反转后的新链表头, curr: 当前处理的节点
9        prev, curr = None, head
10
11        while curr:
12            # 暂存下一个节点
13            temp = curr.next
14
15            # 反转当前节点的指针，指向前一个节点
16            curr.next = prev
17
18            # 移动prev和curr指针，继续处理下一个节点
19            prev = curr
20            curr = temp
21
22        # prev最终指向反转后的链表头
23        return prev
24
25
26# Time Complexity: O(N) - 遍历链表一次，N为节点数
27# Space Complexity: O(1) - 只使用常数个指针变量
28