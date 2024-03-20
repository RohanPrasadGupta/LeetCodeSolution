/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var sortList = function (head) {
  let nums = [];

  while (head) {
    nums.push(head.val);
    head = head.next;
  }
  nums.sort((a, b) => a - b);

  let dummy = new ListNode();
  let cur = dummy;

  for (let num of nums) {
    cur.next = new ListNode(num);
    cur = cur.next;
  }
  return dummy.next;
};

// OR

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var sortList = function (head) {
  if (!head || !head.next) {
    return head;
  }
  let left = head;
  let right = getMid(head);
  let temp = right.next;
  right.next = null;
  right = temp;

  left = sortList(left);
  right = sortList(right);
  return merge(left, right);
};

function getMid(head) {
  let slow = head;
  let fast = head.next;
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }

  return slow;
}

function merge(left, right) {
  let dummy = new ListNode();
  let cur = dummy;

  while (left && right) {
    if (left.val < right.val) {
      cur.next = left;
      left = left.next;
    } else {
      cur.next = right;
      right = right.next;
    }
    cur = cur.next;
  }
  if (left) {
    cur.next = left;
  }
  if (right) {
    cur.next = right;
  }

  return dummy.next;
}
