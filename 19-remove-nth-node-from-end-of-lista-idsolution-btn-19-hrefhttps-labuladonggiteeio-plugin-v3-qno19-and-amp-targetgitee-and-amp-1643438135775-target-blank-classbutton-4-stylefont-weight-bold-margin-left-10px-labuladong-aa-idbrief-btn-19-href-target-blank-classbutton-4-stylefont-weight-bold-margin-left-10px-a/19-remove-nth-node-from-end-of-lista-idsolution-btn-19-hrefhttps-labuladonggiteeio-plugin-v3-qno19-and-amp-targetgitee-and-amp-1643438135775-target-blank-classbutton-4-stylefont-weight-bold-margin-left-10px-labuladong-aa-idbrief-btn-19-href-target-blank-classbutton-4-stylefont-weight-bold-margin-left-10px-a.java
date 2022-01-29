/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // Create a dummy head in case we need to delete the first element
        ListNode dummy = new ListNode();
        dummy.next = head;
        ListNode p1 = dummy;
        ListNode p2 = dummy;
        
        // Use two pointers. When p1 hits the null, p2 will be at the previous 
        // position where the node needs to be removed.
        
        // Let p1 and p2 have a distance n
        for (int i = 0; i < n + 1; i++) {
            p1 = p1.next;
        }
        while (p1 != null) {
            p1 = p1.next;
            p2 = p2.next;
        }
        
        // Remove the nth node
        p2.next = p2.next.next;
        return dummy.next;
    }
}