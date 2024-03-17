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
  // Getting the middle of the Lists
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }

  // Reversing the 2nd half og the list
  let second = slow.next;
  let prev = null;
  slow.next = null;

  while (second) {
    let temp = second.next;
    second.next = prev;
    prev = second;
    second = temp;
  }

  // Now merging the two lists

  let firstHalf = head;
  let secondHalf = prev;
  while (secondHalf) {
    let temp1 = firstHalf.next;
    let temp2 = secondHalf.next;
    firstHalf.next = secondHalf;
    secondHalf.next = temp1;
    firstHalf = temp1;
    secondHalf = temp2;
  }
};
