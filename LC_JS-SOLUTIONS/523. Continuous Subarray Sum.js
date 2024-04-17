/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var checkSubarraySum = function (nums, k) {
  let numSet = new Map();
  numSet.set(0, -1);
  let total = 0;

  for (let i = 0; i < nums.length; i++) {
    total += nums[i];
    let s = total % k;
    if (!numSet.has(s)) {
      numSet.set(s, i);
    } else if (i - numSet.get(s) > 1) {
      return true;
    }
  }
  return false;
};
