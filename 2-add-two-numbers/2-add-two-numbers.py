# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Solution 1:
        # Time complexity: O(n)
        # Space complexity: O(1)
        dummy = ListNode(0)
        p1, p2 = l1, l2
        p = dummy
        
        carry = 0
        while p1 or p2 or carry:
            value = carry
            
            if p1:
                value += p1.val
                p1 = p1.next
            
            if p2:
                value += p2.val
                p2 = p2.next
            
            carry = value // 10
            value = value % 10
            
            p.next = ListNode(value)
            p = p.next
            
        return dummy.next
        