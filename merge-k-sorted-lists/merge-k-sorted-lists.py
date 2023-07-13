# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        size = len(lists)
        if size == 0:
            return None
        if size == 1:
            return lists[0]
        return self.__merge_k_lists(lists, 0, size - 1)

    def __merge_k_lists(self, lists, left, right):
        # divide and conquer
        if left == right:
            return lists[left]
        mid = (left + right) // 2
        left_list = self.__merge_k_lists(lists, left, mid)
        right_list = self.__merge_k_lists(lists, mid + 1, right)
        return self.__merge_two_lists(left_list, right_list)
    
    def __merge_two_lists(self, l1, l2):
        dummy = ListNode()
        p = dummy
        p1, p2 = l1, l2
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        if p1:
            p.next = p1
        elif p2:
            p.next = p2
        return dummy.next