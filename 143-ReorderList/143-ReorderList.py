# Last updated: 1/15/2026, 12:31:27 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reorderList(self, head: Optional[ListNode]) -> None:
8        """
9        Do not return anything, modify head in-place instead.
10        """
11        # Step 1: 用快慢指针找到链表中点
12        slow = fast = head
13
14        while fast and fast.next:
15            slow = slow.next
16            fast = fast.next.next
17
18        # Step 2: 反转后半部分链表
19        prev, curr = None, slow.next
20        while curr:
21            temp = curr.next
22            curr.next = prev
23            prev = curr
24            curr = temp
25        slow.next = None  # 断开前半部分和后半部分
26
27        # Step 3: 交替合并前半部分和反转后的后半部分
28        p1, p2 = head, prev
29        while p2:
30            # 暂存下一个节点
31            next1 = p1.next
32            next2 = p2.next
33
34            # 交替连接：p1 -> p2 -> next1
35            p1.next = p2
36            p1 = next1
37
38            p2.next = p1
39            p2 = next2
40
41
42# Time Complexity: O(N) - 遍历链表三次（找中点 + 反转 + 合并）
43# Space Complexity: O(1) - 只使用常数个指针变量
44