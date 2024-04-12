/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function (root) {
  if (!root) return 0;

  return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
};

// OR DFS SOLUTION

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function (root) {
  if (!root) return 0;

  let res = 1;
  let stack = [[root, 1]];
  while (stack.length) {
    let [node, depth] = stack.pop();
    if (node) {
      res = Math.max(res, depth);
      stack.push([node.left, depth + 1]);
      stack.push([node.right, depth + 1]);
    }
  }
  return res;
};
