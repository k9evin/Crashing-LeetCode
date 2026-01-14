# Last updated: 1/14/2026, 1:48:25 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(
8        self, list1: Optional[ListNode], list2: Optional[ListNode]
9    ) -> Optional[ListNode]:
10        dummy = ListNode()
11        p = dummy
12
13        # 同时遍历两个链表，选择较小的节点接到结果链表
14        while list1 and list2:
15            if list1.val <= list2.val:
16                p.next = list1
17                list1 = list1.next
18            else:
19                p.next = list2
20                list2 = list2.next
21            p = p.next
22
23        # 将剩余的节点直接接到结果链表（至多一个链表有剩余）
24        if list1:
25            p.next = list1
26        if list2:
27            p.next = list2
28
29        # 返回真正的头节点（跳过哨兵节点）
30        return dummy.next
31
32
33# Time Complexity: O(M + N) - M和N分别是两个链表的长度
34# Space Complexity: O(1) - 只使用常数个指针变量，不算返回的链表
35