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
 * @param {number} targetSum
 * @return {boolean}
 */
var hasPathSum = function (root, targetSum) {
  function pathSum(node, curSum) {
    if (!node) return false;

    curSum += node.val;
    if (!node.left && !node.right) {
      return curSum === targetSum;
    }
    return pathSum(node.left, curSum) || pathSum(node.right, curSum);
  }
  return pathSum(root, 0);
};
