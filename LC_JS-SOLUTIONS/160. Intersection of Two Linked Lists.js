/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function (headA, headB) {
  function getLength(head) {
    let length = 0;
    let current = head;
    while (current) {
      length += 1;
      current = current.next;
    }
    return length;
  }

  let lenA = getLength(headA);
  let lenB = getLength(headB);

  let diff = Math.abs(lenA - lenB);

  if (lenA > lenB) {
    for (i = 0; i < diff; i++) {
      headA = headA.next;
    }
  } else if (lenB > lenA) {
    for (i = 0; i < diff; i++) {
      headB = headB.next;
    }
  }

  while (headA && headB) {
    if (headA === headB) {
      return headA;
    }
    headA = headA.next;
    headB = headB.next;
  }
  return null;
};
