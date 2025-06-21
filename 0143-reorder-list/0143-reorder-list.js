/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function (head) {
    let slow = head;
    let fast = head.next;
    // Use slow fast pointers to find the middle of the list
    while (fast !== null && fast.next !== null) {
        slow = slow.next;
        fast = fast.next.next;
    }

    // Split the list and reverse the second half
    let prev = null;
    let curr = slow.next;
    slow.next = null;
    while (curr !== null) {
        let temp = curr.next;
        curr.next = prev;
        prev = curr;
        curr = temp;
    }

    // Merge two lists
    let p1 = head;
    let p2 = prev;
    while (p2 !== null) {
        // Temp store the next values as we will disconnect them
        let temp1 = p1.next;
        let temp2 = p2.next;

        p1.next = p2;
        p2.next = temp1;

        p1 = temp1;
        p2 = temp2;
    }
};