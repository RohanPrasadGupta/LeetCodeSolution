/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function (head) {
  // Funciton to reverse the second half

  function reverseSecHalf(head) {
    let prev = null;
    current = head;
    while (current) {
      let nextNode = current.next;
      current.next = prev;
      prev = current;
      current = nextNode;
    }
    return prev;
  }

  // Inital get the half of the list

  let slow = head;
  let fast = head;

  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }

  // Get the reverse of the 2nd half as slow is pointed to 2nd half

  let revSecHalf = reverseSecHalf(slow);

  // Check the palindrome or not
  let firstHalf = head;

  while (revSecHalf) {
    if (revSecHalf.val != firstHalf.val) {
      return false;
    }
    firstHalf = firstHalf.next;
    revSecHalf = revSecHalf.next;
  }
  return true;
};
